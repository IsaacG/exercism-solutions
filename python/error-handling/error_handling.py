def handle_error_by_throwing_exception():
  raise Exception("Some exception")


def handle_error_by_returning_none(input_data):
  try:
    return int(input_data)
  except:
    return None


def handle_error_by_returning_tuple(input_data):
  try:
    return True, int(input_data)
  except:
    return False, None



def filelike_objects_are_closed_on_exception(filelike_object):
  with filelike_object as f:
    f.do_something()


# vim:ts=2:sw=2:expandtab
