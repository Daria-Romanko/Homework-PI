from yandex_tracker_client import TrackerClient
client = TrackerClient(token = 't1.9euelZqcipuckZKQyZSVlsuOysnHku3rnpWazZ6aypWVjYrNnJaJz46Vy87l8_duN1RT-e8BWjtx_d3z9y5mUVP57wFaO3H9zef1656VmpuTjI_Jz5Gdi4uUi46TmYye7_zF656VmpuTjI_Jz5Gdi4uUi46TmYye.ca--0QA6s8EtXCcfdyUOMotpIX2AgU61YuNIiypbloCvU0768aLj70P0DFHtcEDZqByInO9u0an67PyYNOt3BA', cloud_org_id = 'bpf2nacm2mbsf4s7d2ml')
client.issues.create(
    queue = 'TEAMCITYBUILDFA',
    summary = 'Build fail',
    assignee = 'TEAMCITYBUILDFA'
)
