# country_names = input().split(', ')
# capitals = input().split(', ')
#
# # pair = [country_names: in el for el in capitals]
#
# result = zip(country_names, capitals)
# for a, b in result:
#     print(f'{a} -> {b}')

# second variant:
country_names = input().split(', ')
capitals = input().split(', ')
pair = {country: capital for country, capital in zip(country_names, capitals)}
print("\n".join([f'{a} -> {b}' for a, b in pair.items()]))
