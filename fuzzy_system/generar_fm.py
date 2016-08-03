# el objetivo de este script es el crear funciones para simplificar la creacion
# de los marcos de logica difusa, todos reciben un booleano el cual graficara
# o no el marco, retornan un array con el marco incluido en el

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages # paquete para guardar las graficas
# https://github.com/JDWarner/scikit-fuzzy/blob/scipy2013/scikit-fuzzy_demo.ipynb
import skfuzzy as fuzz  #paquete para logica difusa


def generar_hora(graficar=False):
    # debido que a el paquete de logica difusa no recibe flotantes, se expresara el
    # el tiempo como minutos (entero) 1 dia = 1440 minutos
    # no se toma el minuto 1440, que equivale a 24:00 ya incluido como hora 00:00
    horario = np.arange(0, 1440, 1)

    # Marco hora (Entrada)
    morning = fuzz.trapmf(horario, [0, 0, 480, 720])
    afternoon = fuzz.trapmf(horario, [480, 720, 960, 1200]) # trapecio
    evening = fuzz.trapmf(horario,[960, 1200, 1439, 1439])

    # if graficar:
    #     # graficar el marco
    #     fig, ax = plt.subplots()
    #     ax.plot(horario, morning, 'r', horario, afternoon, 'm', horario, evening, 'b')
    #     ax.set_ylabel('Fuzzy membership')
    #     ax.set_xlabel('Day (Minutes)')
    #     ax.set_ylim(-0.05, 1.05)
    #     ax.set_xlim(0.0, 1400)
    #     #fig.savefig('graphs/hora.png', bbox_inches='tight')
    #
    return {'horario': horario, 'morning': morning,
            'afternoon': afternoon, 'evening': evening}

def generar_actividad(graficar=False):

    # se coloca 11 para que numpy tome efectivamente 11 espacio [0 a 10]
    intensity = np.arange(0, 11, 1)
    # Marco Actividad (Entrada)
    rest = fuzz.trapmf(intensity, [0, 0, 2, 4])
    active = fuzz.trapmf(intensity, [2, 4, 6, 8])
    workout = fuzz.trapmf(intensity, [6, 8, 10, 10])

    # if graficar:
    #     # graficar el marco
    #     fig, ax = plt.subplots()
    #     ax.plot(intensity, rest, 'b', intensity, active, 'y', intensity, workout, 'r')
    #     ax.set_ylabel('Fuzzy membership')
    #     ax.set_xlabel('Activity Intensity (1 - 10)')
    #     ax.set_ylim(-0.05, 1.05)
    #     ax.set_xlim(0.0, 10)
    #     #fig.savefig('graphs/actividad.png', bbox_inches='tight')
    #
    return {'intensity': intensity, 'rest': rest, 'active': active, 'workout': workout}

def generar_clase(graficar=False):

    # se usa para el marco de salida para ver que horario tendra el platillo
    clase = np.arange(0, 11, 1)

    # Marco Pertenencia (Salida)
    breakfast = fuzz.trapmf(clase, [0, 0, 2, 4])
    lunch = fuzz.trapmf(clase, [2, 4, 6, 8])
    dinner = fuzz.trapmf(clase, [6, 8, 10, 10])
    #
    # if graficar:
    #     # graficar el marco
    #     fig, ax = plt.subplots()
    #     ax.plot(clase, breakfast, 'b', clase, lunch, 'y', clase, dinner, 'r')
    #     ax.set_ylabel('Fuzzy membership')
    #     ax.set_xlabel('Dish Classification (1 - 10)')
    #     ax.set_ylim(-0.05, 1.05)
    #     ax.set_xlim(0.0, 10)
    #     #fig.savefig('graphs/clase.png', bbox_inches='tight')

    return {'clase': clase, 'breakfast': breakfast, 'lunch': lunch, 'dinner':dinner}

def generar_calorico(graficar=False):

    # se usa para el marco de salida para ver que horario tendra el platillo
    caloric = np.arange(0, 800, 1)

    # Marco Pertenencia (Salida)
    low = fuzz.trapmf(caloric, [0, 0, 350, 550])
    standard = fuzz.trapmf(caloric, [350, 450, 550, 650])
    high = fuzz.trapmf(caloric, [550, 650, 800, 800])

    # if graficar:
    #     # graficar el marco
    #     fig, ax = plt.subplots()
    #     ax.plot(caloric, low, 'b', caloric, standard, 'y', caloric, high, 'r')
    #     ax.set_ylabel('Fuzzy membership')
    #     ax.set_xlabel('Caloric Classification (Calories)')
    #     ax.set_ylim(-0.05, 1.05)
    #     ax.set_xlim(0, 800)
    #     #fig.savefig('graphs/calorico.png', bbox_inches='tight')

    return {'caloric': caloric, 'low': low, 'standard': standard, 'high':high}

def rule_hora(hour, graficar=False):

    # recibe los datos para poder seguir el proceso difuso para encontrar la pertenencia
    # retorna el valor al que pertenece en la clase segun la hora
    mf_hora = generar_hora(False)
    mf_clase = generar_clase(False)

    # se usa para encontrar los grados de pertenencia del valor, borrificacion
    hora_nivel_morn = fuzz.interp_membership(mf_hora['horario'], mf_hora['morning'], hour)
    hora_nivel_aft = fuzz.interp_membership(mf_hora['horario'], mf_hora['afternoon'], hour)
    hora_nivel_eve = fuzz.interp_membership(mf_hora['horario'], mf_hora['evening'], hour)

    # regla: si manana -> desayuno
    breakfast_activation = np.fmin(hora_nivel_morn, mf_clase['breakfast'])
    # regla: si medio dia -> almuerzo
    lunch_activation = np.fmin(hora_nivel_aft, mf_clase['lunch'])
    # regla: si medio dia -> almuerzo
    dinner_activation = np.fmin(hora_nivel_eve, mf_clase['dinner'])

    # deborrificacion
    agregado = np.fmax(breakfast_activation, np.fmax(lunch_activation, dinner_activation))
    clase = fuzz.defuzz(mf_clase['clase'], agregado, 'centroid')

    # graficar
    # if graficar:
    #     select_clase = fuzz.interp_membership(mf_clase['clase'], agregado, clase)
    #     clase0 = np.zeros_like(mf_clase['clase'])
    #     fig, ax0 = plt.subplots(figsize=(8, 3))
    #
    #     ax0.plot(mf_clase['clase'], mf_clase['breakfast'], 'b', linewidth=0.5, linestyle='--', label='Breakfast')
    #     ax0.plot(mf_clase['clase'], mf_clase['lunch'], 'g', linewidth=0.5, linestyle='--', label='Lunch')
    #     ax0.plot(mf_clase['clase'], mf_clase['dinner'], 'r', linewidth=0.5, linestyle='--', label='Dinner')
    #     ax0.fill_between(mf_clase['clase'], clase0, agregado, facecolor='Orange', alpha=0.7)
    #     ax0.plot([clase, clase], [0, select_clase], 'k', linewidth=1.5, alpha=0.9)
    #     ax0.set_title('Dish Classification and Result (line)')
    #     ax0.legend()
    #     # Turn off top/right axes
    #     for ax in (ax0,):
    #         ax.spines['top'].set_visible(False)
    #         ax.spines['right'].set_visible(False)
    #         ax.get_xaxis().tick_bottom()
    #         ax.get_yaxis().tick_left()
    #
    #     plt.tight_layout()
    #     #fig.savefig('graphs/result_clase.png', bbox_inches='tight')
    #
    return clase, "clase"

def rule_actividad(value, graficar=False):

    # recibe los datos para poder seguir el proceso difuso para encontrar la pertenencia
    # retorna el valor al que pertenece en la clase segun la hora
    mf_actividad = generar_actividad(False)
    mf_calorico = generar_calorico(False)

    # se usa para encontrar los grados de pertenencia del valor, borrificacion
    actividad_nivel_rest = fuzz.interp_membership(mf_actividad['intensity'], mf_actividad['rest'], value)
    actividad_nivel_std = fuzz.interp_membership(mf_actividad['intensity'], mf_actividad['active'], value)
    actividad_nivel_work = fuzz.interp_membership(mf_actividad['intensity'], mf_actividad['workout'], value)

    # regla: si rest -> low
    rest_activation = np.fmin(actividad_nivel_rest, mf_calorico['low'])
    # regla: si active -> std
    active_activation = np.fmin(actividad_nivel_std, mf_calorico['standard'])
    # regla: si workout -> high
    workout_activation = np.fmin(actividad_nivel_work, mf_calorico['high'])

    # deborrificacion
    agregado = np.fmax(rest_activation, np.fmax(active_activation, workout_activation))
    caloric = fuzz.defuzz(mf_calorico['caloric'], agregado, 'centroid')


    # # graficar
    # if graficar:
    #     select_caloric = fuzz.interp_membership(mf_calorico['caloric'], agregado, caloric)
    #     caloric0 = np.zeros_like(mf_calorico['caloric'])
    #     fig, ax0 = plt.subplots(figsize=(8, 3))
    #
    #     ax0.plot(mf_calorico['caloric'], mf_calorico['low'], 'b', linewidth=0.5, linestyle='--', label='Low')
    #     ax0.plot(mf_calorico['caloric'], mf_calorico['standard'], 'g', linewidth=0.5, linestyle='--', label='Standard')
    #     ax0.plot(mf_calorico['caloric'], mf_calorico['high'], 'r', linewidth=0.5, linestyle='--', label='High')
    #     ax0.fill_between(mf_calorico['caloric'], caloric0, agregado, facecolor='Orange', alpha=0.7)
    #     ax0.plot([caloric, caloric], [0, select_caloric], 'k', linewidth=1.5, alpha=0.9)
    #     ax0.set_title('Dish Classification and Result (line)')
    #     ax0.legend()
    #     # Turn off top/right axes
    #     for ax in (ax0,):
    #         ax.spines['top'].set_visible(False)
    #         ax.spines['right'].set_visible(False)
    #         ax.get_xaxis().tick_bottom()
    #         ax.get_yaxis().tick_left()
    #
    #     plt.tight_layout()
    #     #fig.savefig('graphs/result_calorico.png', bbox_inches='tight')
    # 
    return caloric, "caloric"
