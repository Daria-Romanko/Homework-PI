from yandex_tracker_client import TrackerClient

client = TrackerClient(token = 't1.9euelZqSiZiVy8-Ym5LIkJzMlJvIk-3rnpWazZ6aypWVjYrNnJaJz46Vy87l8_dpNFRT-e9-PxJf_d3z9yljUVP5734_El_9zef1656VmpaXlJiPm8-OyYvGlJubnsea7_zF656VmpaXlJiPm8-OyYvGlJubnsea.WHwNTHFBZhCri05l_M5z8pyIDihrQR52qSDDwtMBSV6pozfBODjfq6OnoJ2YOIt6ZqYGnH8rS6-hUrhDwZUmBA', cloud_org_id = 'bpf2nacm2mbsf4s7d2ml')

client.issues.create(
    queue = 'TEAMCITYBUILDFA',
    summary = 'Build fails',
    assignee = 'Daria190404'
)
