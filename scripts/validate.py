import datetime
import gzip
import json
import pathlib
import sys
import xml.etree.ElementTree as ET

path = pathlib.Path(sys.argv[1])
root = ET.parse(path).getroot()
assert root.tag == 'tv', 'Not XMLTV'
selected = {x.attrib['xmltv_id'] for x in ET.parse(sys.argv[2]).getroot()}
now = datetime.datetime.now(datetime.timezone.utc)
current = set()
programs = root.findall('programme')
for p in programs:
    channel = p.attrib['channel']
    assert channel in selected, 'Unexpected channel'
    try:
        start = datetime.datetime.strptime(p.attrib['start'], '%Y%m%d%H%M%S %z')
        stop = datetime.datetime.strptime(p.attrib['stop'], '%Y%m%d%H%M%S %z')
    except (KeyError, ValueError):
        root.remove(p)
        continue
    if stop <= start or not (p.findtext('title') or '').strip():
        root.remove(p)
        continue
    if start <= now < stop:
        current.add(channel)
required = {'TRT 1.tr', 'ATV.tr', 'SHOW TV.tr', 'STAR TV.tr', 'KANAL D.tr'}
assert required <= current, f'Missing current programs: {sorted(required - current)}'
assert len(current) >= 10, 'Insufficient coverage; keeping previous deployment'
programs = root.findall('programme')
ET.ElementTree(root).write(path, encoding='utf-8', xml_declaration=True)
(path.parent / 'tr.xml.gz').write_bytes(gzip.compress(path.read_bytes(), mtime=0))
(path.parent / 'status.json').write_text(json.dumps({'updated': now.isoformat(), 'channels': len(current), 'programs': len(programs)}, indent=2))
print(f'Validated {len(current)} current channels and {len(programs)} programs')
