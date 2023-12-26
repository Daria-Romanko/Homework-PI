from yandex_tracker_client import TrackerClient

client = TrackerClient(token = 'y0_AgAAAAA_Po2UAAsNAQAAAAD2ABOKFzFo5IiaRv6780PAmc2Pa0yfh3E', cloud_org_id = 'bpf2nacm2mbsf4s7d2ml')

client.issues.create(
    queue = 'TEAMCITYBUILDFA',
    summary = 'Build fails',
    assignee = 'Дарья Р.'
)
