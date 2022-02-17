
from eyeroll.gpio.pwm_generate import WesPWM
import pigpio

if __name__ == "__main__":
    pi = pigpio.pi()
    s1 = WesPWM(pi, 5, double_range=True)
    s2 = WesPWM(pi, 6, double_range=True)
    s3 = WesPWM(pi, 26, double_range=True)
