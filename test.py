from LoR.main import get_random_index_sha256, get_random_form_list

print(f"{get_random_index_sha256(32)}")  # Result should be 0.0
print(f"{get_random_form_list([1, 2, 3, 4, 5, 6, 7])}")  # Result should be 32.0
