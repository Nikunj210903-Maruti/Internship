from properties.p import Property
prop = Property()
dic_prop = prop.load_property_files('sql.properties')
print(dic_prop['key'])