from yandex_tracker_client import TrackerClient

client = TrackerClient(token = 'y0_AgAAAAA_Po2UAATuwQAAAAD190GIqbXrdLKKSHqsz5VJVLgN-3os8Wc', cloud_org_id = 'bpf2nacm2mbsf4s7d2ml')

client.issues.create(
    queue = 'TEAMCITYBUILDFA',
    summary = 'Build fails',
    assignee = 'Daria190404'
)
