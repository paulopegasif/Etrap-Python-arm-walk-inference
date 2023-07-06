from __future__ import division
import time
import Adafruit_PCA9685
import serial
import os

pwm = Adafruit_PCA9685.PCA9685()

nomeServo = ""


serv = [0,4,8,12,15]
value = [375, 500, 500, 210, 450]
order = [2,1,0,3,4]
inicio = [1,2,0,4,3]

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096



# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
    
# Function for the print values
    

# Set frequency to 60hz, good for servos.

pwm.set_pwm_freq(60)


count = 0
var_exit = 0

# Initial Position

print("# AGUARDE # - Posicionando...")

value = [375, 500, 500, 210, 450]

            
time.sleep(1)

for i in range(4):
    pwm.set_pwm(serv[i], 0, int(value[i]))
    time.sleep(0.5)
    


while True:
    #Clear
    os.system('clear')
        
    print("0 - Mover Base (0-255)")
    print("-----------------------")
    print("1 - Mover Ombro (150-600)")
    print("-----------------------")
    print("2 - Mover Cotovelo (150 - 600)")
    print("-----------------------")
    print("3 - Mover Punho (150-600)")
    print("-----------------------")
    print("4 - Mover Mao (150-600)")
    print("-----------------------")
    print("5 - Sair")
    print("-----------------------")
    print("### VALORES ATUAIS ###")
    print("Base:" + str(value[0]))
    print("Ombro:" + str(value[1]))
    print("Cotovelo:" + str(value[2]))
    print("Punho:" + str(value[3]))
    print("Mao:" + str(value[4]))
    
    print("\n")
    escolha = int(input("Opcao:"))
    if escolha==0:
        
        var_exit = 0
        print("MAIOR = Esquerda")
        print("MENOR = Direita")
        print("---------------")
        print("Valor atual|BASE:" + str(value[0]))
        value[0] = int(input("Valor:"))
        ser.flushInput()
        while var_exit < 10:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                if int(line) == (value[0]):
                    pwm.set_pwm(serv[0], 0, 633)
                    var_exit = var_exit + 1
                elif int(line) > (value[0]):
                    pwm.set_pwm(serv[0], 0, 628)
                    var_exit = 0
                else: 
                    pwm.set_pwm(serv[0], 0, 638)
                    var_exit = 0
                print(line)
                
    if escolha==1:
        print("MAIOR = TRAS")
        print("MENOR = FRENTE")
        print("---------------")
        #print("Valor atual:" + str(value[0]))
        print("Valor atual|OMBRO:" + str(value[escolha]))
        antes = value[escolha]
        value[escolha] = int(input("valor:"))
        for i in range(antes, 550):
                pwm.set_pwm(serv[escolha], 0, i)
                time.sleep(0.01)
                print(i)
        for i in range(550, value[escolha], -1):
            pwm.set_pwm(serv[escolha], 0, i)
            time.sleep(0.01)
            print(i)
                
    elif escolha<5 and escolha>1:
        
        if escolha == 2:
            nomeServo = "COTOVELO"
            print("MENOR = CIMA")
            print("MAIOR = BAIXO")
        elif escolha == 3:
            nomeServo = "PUNHO"
            print("MENOR = ESQUERDA")
            print("MAIOR = DIREITA")
        elif escolha == 4:
            nomeServo = "MAO"
            print("MENOR = BAIXO")
            print("MAIOR = CIMA")
        
        print("---------------")
        print("Valor atual|" + nomeServo + ":" + str(value[escolha]))
        antes = value[escolha]
        value[escolha] = int(input("valor:"))
        if value[escolha] > antes:
            for i in range(antes, value[escolha]):
                pwm.set_pwm(serv[escolha], 0, i)
                time.sleep(0.01)
                print(i)
        else:
            for i in range(antes, value[escolha], -1):
                pwm.set_pwm(serv[escolha], 0, i)
                time.sleep(0.01)
                print(i)
        #pwm.set_pwm(serv[escolha-1], 0, int(value[escolha-1]))
    elif escolha == 5:
        exit()
        
