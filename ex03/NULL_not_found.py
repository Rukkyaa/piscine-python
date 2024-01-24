def NULL_not_found(object: any) -> int:
  null_types = [None, 0, "", False]

  if object in null_types or str(object) == "nan":
    print(type(object))
    return 0

  print(f"{type(object)} is not a null type")
  return 1