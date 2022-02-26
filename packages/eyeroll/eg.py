
from eyeroll.gpio.pwm_generate import WesPWM
import pigpio
import time

def exercise_1(sn, N=100, dt=0.03):
    sn.goto(-1)
    time.sleep(.15)
    for n in range(N):
        sn.goto(-1 + 2 * float(n) / N)
        time.sleep(dt)
    time.sleep(.15)
    sn.zero()

def n_sign(n):
    return [1., -1][n%2]

def exercise_2(sns, N=100, dt=0.03):
    for n, sn in enumerate(sns):
        sn.goto(.5*n_sign(n))
    time.sleep(.15)
    for n in range(N):
        for nn, sn in enumerate(sns):
            sn.goto(n_sign(nn)*(.5 - float(n) / N))
        time.sleep(dt)
    for n in range(N):
        for nn, sn in enumerate(sns):
            sn.goto(-n_sign(nn)*(.5 - float(n) / N))
        time.sleep(dt)
    time.sleep(.15)
    for sn in sns:
        sn.zero()


if __name__ == "__main__":
    pi = pigpio.pi()
    s1 = WesPWM(pi, 5, double_range=True)
    s2 = WesPWM(pi, 6, double_range=True)
    s3 = WesPWM(pi, 26, double_range=True)

    s1.zero(); s2.zero(); s3.zero()
    time.sleep(.5)

    exercise_1(s1)
    exercise_1(s2)
    exercise_1(s3)
    exercise_2([s1, s2, s3])
    s1.zero(); s2.zero(); s3.zero()
    time.sleep(.5)
