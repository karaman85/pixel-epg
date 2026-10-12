# Pixel Türkiye EPG

Türkiye kanalları için iptv-org/epg ve Digiturk yayın akışı kaynağıyla XMLTV üretimi.

GitHub Actions günde dört kez (İstanbul saati 05:17, 11:17, 17:17, 23:17; çalışma gecikebilir) iki günlük rehber üretir. Güncel TRT 1, ATV, Show TV, Star TV ve Kanal D verisi yoksa yayınlama durur; önceki rehber korunur. Kalite sürümleri için tek kanal kimliği kullanılır. NOW, kaynağın FOX olarak adlandırdığı kayıttan alınır; canlı içerik kontrolü gereklidir.

GitHub Pages kaynağı Settings → Pages → GitHub Actions olarak ayarlanmalıdır. İlk başarılı çalışmadan sonra EPG adresi Pages adresine `/tr.xml` eklenerek bulunur. Gzip sürümü `/tr.xml.gz`, son başarılı üretim özeti `/status.json` adresindedir.

Sadece bu klasör yayımlanır. IPTV listeleri, yayın adresleri, kullanıcı bilgileri veya uygulama kodu içermez. İlk canlı üretim ve uygulama eşleşmesi doğrulanmadan kaynak çalışır kabul edilmez.

Upstream: https://github.com/iptv-org/epg (sürüm UPSTREAM_REVISION dosyasında sabitlenir). Program verileri ilgili kaynaklardan gelir; kod lisansı veri haklarını belirlemez.
