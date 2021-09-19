import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

contrast = ctrl.Antecedent(np.arange(0, 89, 0.5), 'contrast')
lighting = ctrl.Antecedent(np.arange(0, 89,  0.5), 'lighting')
size = ctrl.Consequent(np.arange(0, 100,  0.5), 'size')

# Fuzzifikasi

contrast['low'] = fuzz.trimf(contrast.universe, [12, 30, 33])
contrast['medium'] = fuzz.trimf(contrast.universe, [35, 36, 40])
contrast['high'] = fuzz.trimf(contrast.universe, [43, 50, 60])

lighting['low'] = fuzz.trimf(lighting.universe, [12, 30, 33])
lighting['medium'] = fuzz.trimf(lighting.universe,  [35, 36, 40])
lighting['high'] = fuzz.trimf(lighting.universe, [43, 50, 60])

size['low'] = fuzz.trimf(size.universe, [34, 44, 55])
size['medium'] = fuzz.trimf(size.universe, [55, 66, 77])
size['high'] = fuzz.trimf(size.universe, [77, 88, 99])

contrast.view()
lighting.view()
size.view()

# inferensi

rule1 = ctrl.Rule(contrast['low'] & lighting['low'], size['low'])
rule2 = ctrl.Rule(contrast['low'] & lighting['high'], size['low'])

rule3 = ctrl.Rule(contrast['medium'] & lighting['low'], size['low'])
rule4 = ctrl.Rule(contrast['medium'] & lighting['high'], size['high'])

rule5 = ctrl.Rule(contrast['high'] & lighting['low'], size['high'])
rule6 = ctrl.Rule(contrast['high'] & lighting['high'], size['high'])

plt.show()