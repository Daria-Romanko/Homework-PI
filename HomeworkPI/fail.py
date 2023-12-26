from yandex_tracker_client import TrackerClient
client = TrackerClient(token = 't1.9euelZqMipmYjcnHmpzLi5HMlJuMxu3rnpWazZ6aypWVjYrNnJaJz46Vy87l8_ceRFVT-e8_eRRf_d3z915yUlP57z95FF_9zef1656VmpaajcvNlI2Wj52eiY2Nx8ia7_zF656VmpaajcvNlI2Wj52eiY2Nx8ia.1W0FhYKz8_STJM8LntypZylDAwZXBkKn7hlatR2Y6jbt55Lps2Vksp-AKdfCkMN4oZGdKwE5HcVMnpgbgoPxDA', cloud_org_id = 'bpf2nacm2mbsf4s7d2ml')
client.issues.create(
    queue = 'TEAMCITYBUILDFA',
    summary = 'Build fail',
    assignee = 'TEAMCITYBUILDFA'
)
