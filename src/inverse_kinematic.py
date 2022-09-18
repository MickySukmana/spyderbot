import numpy as np

class inverse_kinematic:
	def __init__(self, _l1, _l2):
		self.l1 = _l1
		self.l2 = _l2

	def calc(self, x, y, z):
		l1 = self.l1
		l2 = self.l2

		theta1 = np.arctan2(y,x)
		r = np.sqrt(x**2+y**2)
		
		r2 = r**2+z**2
		c2 = (r2-l1**2-l2**2)/(2*l1*l2)
		a = np.arccos(-(r2-l1**2-l2**2)/(2*l1*l2))
		s2 = np.sqrt(1-c2**2)

		theta3 = np.pi-a

		b = np.arctan2(l2*s2, l1+(l2*c2))
		c = np.arctan2(z, r)

		theta2 = c - b
		
		print(np.rad2deg(theta1))
		print(np.rad2deg(theta2))
		print(np.rad2deg(theta3))
		
		return theta1, theta2, theta3
