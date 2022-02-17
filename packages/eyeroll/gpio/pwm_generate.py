import pigpio


class WesPWM:
    HW_PWM = 1
    SW_PWM = 0

    def __init__(self, pi, gpio, frequency=100, double_range=True):
        self.pi = pi
        self.gpio = gpio

        self.pi.set_mode(gpio, pigpio.OUTPUT)
        self.frequency = frequency
        self.duty = None
        self.position = 0.

        self._double_range = double_range

        if False and gpio in {12, 13, 18, 19}:  # "HW PWM only supported gpio pins: 12, 13, 18, 19"
            self.type = self.HW_PWM
            self._init_hw_pwm()
        else:
            self.type = self.SW_PWM
            self._init_sw_pwm()

    def _init_hw_pwm(self):
        self.full_range = 1000000
        self.zero_duty = int( (3 * 1000000) / (2*20) )  # 1M = 20 msec
        self.half_range = int(self.zero_duty / 3)
        if self._double_range:
            self.half_range *= 2
        self.duty = self.zero_duty
        self.goto(0)

    def _init_sw_pwm(self):
        # default sample rate is 5 us yielding possible PWM frequencies of:
        #  8000 4000 2000 1600 1000 ... 50 40 20 10 ... 20 is what we want.
        #  http://abyz.me.uk/rpi/pigpio/python.html#set_PWM_frequency
        self.full_range = 10000  # max range resolution is 40000
        self.zero_duty = 1500
        self.half_range = 500
        if self._double_range:
            self.half_range *= 2
        self.duty = self.zero_duty
        self.pi.set_PWM_frequency(self.gpio, self.frequency)
        self.pi.set_PWM_range(self.gpio, self.full_range)
        self.pi.set_PWM_dutycycle(self.gpio, self.zero_duty)

    def zero(self):
        self.goto(0)

    def goto(self, value):
        """
        Set the value of the servo duty cycle
        :param value: -1 to +1
        :return:
        """
        self.duty = int(value * self.half_range) + self.zero_duty
        if self.type == self.HW_PWM:
            self.pi.hardware_PWM(self.gpio, self.frequency, self.duty)
        else:
            self.pi.set_PWM_dutycycle(self.gpio, self.duty)

        self.position = value
        return self.position