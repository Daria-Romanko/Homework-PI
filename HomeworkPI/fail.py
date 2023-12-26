from yandex_tracker_client import TrackerClient

client = TrackerClient(token = 'y0_AgAAAAA_Po2UAAsM_AAAAAD1_81tE_H9g3cpShOuOXR902B6NwNgAuU', cloud_org_id = 'bpf2nacm2mbsf4s7d2ml')

client.issues.create(
    queue = 'TEAMCITYBUILDFA',
    summary = 'Build fails',
    assignee = 'Daria190404'
)
