from yandex_tracker_client import TrackerClient

client = TrackerClient(token = 't1.9euelZrMjsiKxo2Yx87NyY_OicyTie3rnpWazZ6aypWVjYrNnJaJz46Vy87l8_cmLVRT-e8nOx1u_N3z92ZbUVP57yc7HW78zef1656VmpKRnZ7GkcedmpmPkcvNycnG7_zF656VmpKRnZ7GkcedmpmPkcvNycnG.IrF2MMj32zy1TJvvrFMrpljvSitBUc2U19rQ3B5yVKMv4Tb_7S71ZSiE2dLvZUcv2l8sTMWxk1UhuUHPZPRMDw', cloud_org_id = 'bpf2nacm2mbsf4s7d2ml')

client.issues.create(
    queue = 'TEAMCITYBUILDFA',
    summary = 'Build fails',
    assignee = 'Daria190404'
)
