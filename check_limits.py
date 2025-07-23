
def battery_is_ok(temperature, soc, charge_rate):
  if not (0 <= temperature <=45 and 20 <= soc <=80 and charge_rate <= 0.8):
    print('Temperature, State of Charge and Charge Rate is out of range!')
    return False
  return True

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
