import math

def main():
    rho, mu, q, l, d, k = get_info()
    g = 9.8
    v = q_to_v(q, d)
    re = Re(rho, mu, v, d)
    f = fric_coef(re, k, d)
    dP = h_f(f, v, l, g, d)
    print(f'The pressure drop is estimated to be {round(dP, 2)} [Pa] or {round(dP/101325, 4)} [atm].')
    print(f'While the friction factor is estimated to be {round(f, 5)}.')

def get_info():
    rho_g = float(input('What is the density of the fluid? [kg/m^3] '))
    if rho_g <= 0:
        raise ValueError('Density cannot be non-positive')
    mu_g = float(input('What is the dynamic viscosity of the fluid? [Pa*sec] '))
    if mu_g <= 0:
        raise ValueError('Viscosity cannot be non-positive')
    q_g = float(input('What is the flow rate of the fluid? [m^3/sec] '))
    if q_g <= 0:
        raise ValueError('Flow rate cannot be non-positive')
    l_g = float(input('What is the length of the pipe? [m] '))
    if l_g <= 0:
        raise ValueError('Length cannot be non-positive')
    d_g = float(input('What is the diameter of the pipe? [m] '))
    if d_g <= 0:
        raise ValueError('Diameter cannot be non-positive')
    k_g = float(input('What is the surface roughness of the pipe? [m] '))
    if k_g <= 0:
        raise ValueError('Surface roughness cannot be non-positive')
    return rho_g, mu_g, q_g, l_g, d_g, k_g

def q_to_v(Q, D):
    return 4*Q/(math.pi*D**2)

def Re(Rho, Mu, V, D):
    RE = Rho*V*D/Mu
    if 2000 < RE < 4000 or RE > 5*10**8:
        raise Exception("Sorry, the Reynolds number of the problem is not suitable for the approximation model")
    return RE

def fric_coef(Re, K, D):
    epsilon = K/D
    if epsilon > 0.01:
        raise Exception("Sorry, the surface roughness to the diameter ration of the problem is not suitable for the "
                        "approximation model")
    if 0 < Re <= 2000:
        return 64/Re
    else:
        return 0.0055*(1+(2*10**4 * epsilon + 10**6/Re)**(1/3))

def h_f(F, V, L, G, D):
    return (F*L*V**2)/(2*G*D)




if __name__ == "__main__":
    main()