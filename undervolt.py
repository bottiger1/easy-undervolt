MAX_CLOCK = input('Max clock in MHZ (ie 1700): ')
MAX_VOLTAGE = input('Max voltage in mV (ie 700): ')

MAX_CLOCK = int(MAX_CLOCK)
MAX_VOLTAGE = int(MAX_VOLTAGE)

import xml.etree.ElementTree as ET

tree = ET.parse('default.xml')
root = tree.getroot()
profile = root[0][1][0]

data = profile.attrib

i = 0
while 1:
	if 'GPUVolOffset%i' % i not in data:
		break

	voltage = int(data['GPUVolOffset%i' % i])
	if voltage >= MAX_VOLTAGE:
		data['GPUClkOffset%i' % i] = str(MAX_CLOCK)
		data['GPUVolOffset%i' % i] = str(MAX_VOLTAGE)

	# swap voltage and clock
	clock = data['GPUClkOffset%i' % i]
	voltage = data['GPUVolOffset%i' % i]

	data['GPUClkOffset%i' % i] = voltage
	data['GPUVolOffset%i' % i] = clock

	i += 1

tree.write('new.xml')