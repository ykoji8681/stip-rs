
# URLを正規表現で評価し、マッチングした場合の処理箇所を定義
from django.conf.urls import url
import ctirs.api.v1.stix_files.views as stix_files

urlpatterns = [
    # STIX 取得
    url(r'^(?P<id_>\S+)/stix$', stix_files.stix_files_id_stix),
    # STIX ファイル情報取得/削除
    url(r'^(?P<id_>\S+)$', stix_files.stix_files_id),
]
