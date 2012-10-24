import nose.tools as n
import lib

class TestConversion:
    def _(self, orig, expected):
        observed = lib.convert(orig)
        n.assert_equal(observed, expected)

    def test1(self):
        self._('Z5.x05.q0+L', 85)

    def test_calculator(self):
        self._('z5.x90.q0', 90)

    def test_s3_calculator_best(self):
        self._('z5.x50.q0+L', 50)

    def test_s4_car_best(self):
        self._('z5.x05.q0+l', 5)

    def test_s2_calculator_worst(self):
        self._('z0.x60.q3+l', )

    def test_s__best(self):
        self._('', )

    def test_s__worst(self):
        self._('', )

    def test_s__best(self):
        self._('', )

    def test_s__worst(self):
        self._('', )

    def test_s__best(self):
        self._('', )

    def test_s__worst(self):
        self._('', )

    def test_s__best(self):
        self._('', )

    def test_s__worst(self):
        self._('', )

    def test_s__best(self):
        self._('', )

    def test_s__worst(self):
        self._('', )

    def test_s__best(self):
        self._('', )

    def test_s__worst(self):
        self._('', )

    def test1(self):
        self._('', )
