from yandex_tracker_client import TrackerClient

client = TrackerClient(token = 't1.9euelZqMipmYjcnHmpzLi5HMlJuMxu3rnpWazZ6aypWVjYrNnJaJz46Vy87l8_cTMlRT-e9KTEkK_t3z91NgUVP570pMSQr-zef1656VmpqJzMjJj5yTnpqQj5iTiYqT7_zF656VmpqJzMjJj5yTnpqQj5iTiYqT.SLglAlV3k5nYFn7I8JsFHCIS-fTu7idEZ3APS5LZvOm5QT_n98Z9WavVOn0B0jv9XgE_0TLMsj30-ZP_44VzDA', cloud_org_id = 'bpf2nacm2mbsf4s7d2ml')

client.issues.create(
    queue = 'TEAMCITYBUILDFA',
    summary = 'Build fails',
    assignee = 'Daria190404'
)
