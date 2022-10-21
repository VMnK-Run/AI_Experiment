"""A set of example unit tests.
NOTE: Do not rely on these tests as they are just simple examples.
Your code will be tested on some secret instances of the problems!
"""

import unittest
from hmm import HMM
import numpy as np


class TestHMM(unittest.TestCase):

    def setUp(self):
        """Sets the seed of the random number generator to produce the same tests.
        """
        np.random.seed(0)
        kwargs = {
            'width': 16,
            'length': 16,
            'rssi_range': 4,
            'n_beacons': 4,
            'init_pos': (0, 0)
        }
        self.model = HMM(**kwargs)
        self.T = 1 << 7  # Time steps
        actual_path, observations = self.model.generate_path(self.T)
        self.actual_path = actual_path
        self.observations = observations

    def test_predict(self):
        """Tests the method predict.
        """
        probs = self.model.predict(self.model.init_probs)
        err = np.sqrt(((probs / np.sum(probs) - predicted_probs / np.sum(predicted_probs)) ** 2).mean())
        self.assertAlmostEqual(0, err, delta=1e-9)

    def test_update(self):
        """Tests the method update.
        """
        probs = self.model.update(self.model.init_probs, self.observations[1])
        err = np.sqrt(((probs / np.sum(probs) - updated_probs / np.sum(updated_probs)) ** 2).mean())
        self.assertAlmostEqual(0, err, delta=1e-9)

    def test_monitor(self):
        """Tests the method monitor.
        """
        probs = self.model.monitor(self.T, self.observations)[-1]
        err = np.sqrt(((probs / np.sum(probs) - monitoring_probs / np.sum(monitoring_probs)) ** 2).mean())
        self.assertAlmostEqual(0, err, delta=1e-9)

    def test_postdict(self):
        """Tests the method postdict.
        """
        probs = self.model.postdict(self.model.init_probs)
        err = np.sqrt(((probs / np.sum(probs) - postdict_probs / np.sum(postdict_probs)) ** 2).mean())
        self.assertAlmostEqual(0, err, delta=1e-9)

    def test_backwards(self):
        """Tests the method backwards.
        """
        probs = self.model.backwards(self.T, self.observations)[0]
        err = np.sqrt(((probs / np.sum(probs) - backwards_probs / np.sum(backwards_probs)) ** 2).mean())
        self.assertAlmostEqual(0, err, delta=1e-9)

    def test_hindsight(self):
        """Tests the method hindsight.
        """
        probs = self.model.hindsight(self.T, self.observations)[self.T // 2]
        err = np.sqrt(((probs / np.sum(probs) - hindsight_probs / np.sum(hindsight_probs)) ** 2).mean())
        self.assertAlmostEqual(0, err, delta=1e-9)


if __name__ == '__main__':
    unittest.main()

predicted_probs = np.array([
    3.22106835e-01, 1.95385968e-01, 4.36238022e-02, 3.61243679e-03,
    1.42340470e-04, 3.54763870e-05, 3.42798058e-05, 3.42748614e-05,
    3.42748540e-05, 3.42749006e-05, 3.42761197e-05, 3.42958542e-05,
    3.44904979e-05, 3.54931201e-05, 3.67199135e-05, 3.03735630e-05,
    1.95385968e-01, 1.18529701e-01, 2.64805550e-02, 2.21183118e-03,
    1.06994113e-04, 4.21658819e-05, 4.14393843e-05, 4.14363573e-05,
    4.14363528e-05, 4.14364091e-05, 4.14378830e-05, 4.14617409e-05,
    4.16970540e-05, 4.29091674e-05, 4.43922910e-05, 3.67199135e-05,
    4.36238022e-02, 2.64805550e-02, 5.94051175e-03, 5.24526352e-04,
    5.46987742e-05, 4.02159032e-05, 4.00527038e-05, 4.00519866e-05,
    4.00519856e-05, 4.00520400e-05, 4.00534647e-05, 4.00765255e-05,
    4.03039769e-05, 4.14755941e-05, 4.29091674e-05, 3.54931201e-05,
    3.61243679e-03, 2.21183118e-03, 5.24526352e-04, 7.89128489e-05,
    4.01446969e-05, 3.89353540e-05, 3.89206903e-05, 3.89205830e-05,
    3.89205829e-05, 3.89206358e-05, 3.89220202e-05, 3.89444296e-05,
    3.91654559e-05, 4.03039769e-05, 4.16970540e-05, 3.44904979e-05,
    1.42340470e-04, 1.06994113e-04, 5.46987742e-05, 4.01446969e-05,
    3.87608956e-05, 3.87027704e-05, 3.87009928e-05, 3.87009386e-05,
    3.87009386e-05, 3.87009911e-05, 3.87023677e-05, 3.87246507e-05,
    3.89444296e-05, 4.00765255e-05, 4.14617409e-05, 3.42958542e-05,
    3.54763870e-05, 4.21658819e-05, 4.02159032e-05, 3.89353540e-05,
    3.87027704e-05, 3.86801021e-05, 3.86787218e-05, 3.86786693e-05,
    3.86786693e-05, 3.86787218e-05, 3.86800977e-05, 3.87023677e-05,
    3.89220202e-05, 4.00534647e-05, 4.14378830e-05, 3.42761197e-05,
    3.42798058e-05, 4.14393843e-05, 4.00527038e-05, 3.89206903e-05,
    3.87009928e-05, 3.86787218e-05, 3.86773460e-05, 3.86772935e-05,
    3.86772935e-05, 3.86773460e-05, 3.86787218e-05, 3.87009911e-05,
    3.89206358e-05, 4.00520400e-05, 4.14364091e-05, 3.42749006e-05,
    3.42748614e-05, 4.14363573e-05, 4.00519866e-05, 3.89205830e-05,
    3.87009386e-05, 3.86786693e-05, 3.86772935e-05, 3.86772410e-05,
    3.86772410e-05, 3.86772935e-05, 3.86786693e-05, 3.87009386e-05,
    3.89205829e-05, 4.00519856e-05, 4.14363528e-05, 3.42748540e-05,
    3.42748540e-05, 4.14363528e-05, 4.00519856e-05, 3.89205829e-05,
    3.87009386e-05, 3.86786693e-05, 3.86772935e-05, 3.86772410e-05,
    3.86772410e-05, 3.86772935e-05, 3.86786693e-05, 3.87009386e-05,
    3.89205829e-05, 4.00519856e-05, 4.14363528e-05, 3.42748540e-05,
    3.42749006e-05, 4.14364091e-05, 4.00520400e-05, 3.89206358e-05,
    3.87009911e-05, 3.86787218e-05, 3.86773460e-05, 3.86772935e-05,
    3.86772935e-05, 3.86773460e-05, 3.86787218e-05, 3.87009911e-05,
    3.89206358e-05, 4.00520400e-05, 4.14364091e-05, 3.42749006e-05,
    3.42761197e-05, 4.14378830e-05, 4.00534647e-05, 3.89220202e-05,
    3.87023677e-05, 3.86800977e-05, 3.86787218e-05, 3.86786693e-05,
    3.86786693e-05, 3.86787218e-05, 3.86800977e-05, 3.87023677e-05,
    3.89220202e-05, 4.00534647e-05, 4.14378830e-05, 3.42761197e-05,
    3.42958542e-05, 4.14617409e-05, 4.00765255e-05, 3.89444296e-05,
    3.87246507e-05, 3.87023677e-05, 3.87009911e-05, 3.87009386e-05,
    3.87009386e-05, 3.87009911e-05, 3.87023677e-05, 3.87246507e-05,
    3.89444296e-05, 4.00765255e-05, 4.14617409e-05, 3.42958542e-05,
    3.44904979e-05, 4.16970540e-05, 4.03039769e-05, 3.91654559e-05,
    3.89444296e-05, 3.89220202e-05, 3.89206358e-05, 3.89205829e-05,
    3.89205829e-05, 3.89206358e-05, 3.89220202e-05, 3.89444296e-05,
    3.91654559e-05, 4.03039769e-05, 4.16970540e-05, 3.44904979e-05,
    3.54931201e-05, 4.29091674e-05, 4.14755941e-05, 4.03039769e-05,
    4.00765255e-05, 4.00534647e-05, 4.00520400e-05, 4.00519856e-05,
    4.00519856e-05, 4.00520400e-05, 4.00534647e-05, 4.00765255e-05,
    4.03039769e-05, 4.14755941e-05, 4.29091674e-05, 3.54931201e-05,
    3.67199135e-05, 4.43922910e-05, 4.29091674e-05, 4.16970540e-05,
    4.14617409e-05, 4.14378830e-05, 4.14364091e-05, 4.14363528e-05,
    4.14363528e-05, 4.14364091e-05, 4.14378830e-05, 4.14617409e-05,
    4.16970540e-05, 4.29091674e-05, 4.43922910e-05, 3.67199135e-05,
    3.03735630e-05, 3.67199135e-05, 3.54931201e-05, 3.44904979e-05,
    3.42958542e-05, 3.42761197e-05, 3.42749006e-05, 3.42748540e-05,
    3.42748540e-05, 3.42749006e-05, 3.42761197e-05, 3.42958542e-05,
    3.44904979e-05, 3.54931201e-05, 3.67199135e-05, 3.03735630e-05
])

updated_probs = np.array([
    6.68577841e-02, 2.98881138e-06, 1.26071548e-06, 1.36669487e-07,
    8.98128759e-09, 3.18395509e-09, 2.43130445e-09, 4.97753475e-09,
    4.22200915e-08, 1.84006412e-07, 2.77378544e-07, 2.48338916e-07,
    1.21235105e-07, 6.48884332e-08, 3.05076143e-08, 2.03759327e-08,
    1.36403890e-06, 1.71166412e-06, 8.59808341e-07, 1.35585769e-07,
    1.05568031e-08, 2.52896107e-09, 2.73188915e-09, 7.57205185e-09,
    5.75276012e-08, 2.09632364e-07, 3.01206017e-07, 2.46880620e-07,
    1.31746496e-07, 1.05674146e-07, 1.02603770e-07, 1.08400239e-07,
    5.62294389e-07, 7.48030918e-07, 4.08849772e-07, 8.07319598e-08,
    6.77514386e-09, 8.46506563e-10, 1.23633320e-09, 5.84637604e-09,
    5.21790140e-08, 1.73783693e-07, 2.17107904e-07, 1.45174962e-07,
    9.33352295e-08, 1.41275028e-07, 2.35313736e-07, 2.88457492e-07,
    2.80489032e-07, 2.63321197e-07, 1.02160190e-07, 1.77022358e-08,
    1.55708709e-09, 1.09288550e-10, 1.50695675e-10, 1.09002966e-09,
    1.35413044e-08, 5.81269310e-08, 8.35585219e-08, 6.15604651e-08,
    6.55915388e-08, 1.13517680e-07, 1.68102049e-07, 2.00372441e-07,
    2.59603611e-07, 1.28165591e-07, 3.39521061e-08, 6.37130480e-09,
    8.44561560e-10, 6.47830062e-11, 1.48636575e-11, 5.21855089e-11,
    6.96124267e-10, 5.07502519e-09, 1.50695619e-08, 3.23165084e-08,
    1.02125251e-07, 1.20958425e-07, 7.75751791e-08, 6.60367211e-08,
    2.51459948e-07, 1.93923657e-07, 9.65119495e-08, 2.90652895e-08,
    5.22945856e-09, 4.73625006e-10, 3.17253540e-11, 1.43216410e-11,
    7.91387731e-11, 5.07068622e-10, 3.83982062e-09, 7.68487578e-08,
    4.62830923e-07, 4.21339057e-07, 1.33114435e-07, 4.90539295e-08,
    4.67778859e-07, 5.00308631e-07, 3.22507304e-07, 1.10758584e-07,
    2.72608582e-08, 4.76411717e-09, 4.69846120e-10, 6.95370730e-11,
    1.94965462e-10, 8.49819376e-10, 5.52456676e-09, 1.14855397e-07,
    6.72624639e-07, 6.07244967e-07, 1.81620187e-07, 5.54815706e-08,
    8.72545340e-07, 8.97597351e-07, 5.27702072e-07, 1.57316223e-07,
    4.75612795e-08, 1.92965894e-08, 5.73022229e-09, 1.75668275e-09,
    3.82292696e-09, 7.89391571e-09, 1.05644720e-08, 3.39668149e-08,
    1.51854646e-07, 2.26813570e-07, 1.53505419e-07, 9.50704501e-08,
    8.58779497e-07, 8.92567335e-07, 4.83102201e-07, 1.07279300e-07,
    3.20493472e-08, 2.35129427e-08, 2.17788738e-08, 4.01305227e-08,
    7.50828611e-08, 7.19162851e-08, 3.48386286e-08, 1.40288123e-08,
    2.27647620e-08, 6.52583694e-08, 9.28397212e-08, 8.03136540e-08,
    3.16558384e-07, 3.88595220e-07, 2.16676127e-07, 4.07787450e-08,
    1.01348367e-08, 1.17487325e-08, 4.36118890e-08, 2.94214421e-07,
    6.50186945e-07, 4.18848868e-07, 1.42466783e-07, 3.47723122e-08,
    1.22528015e-08, 1.17085579e-08, 1.45794670e-08, 1.42371508e-08,
    8.64465654e-08, 8.74850390e-08, 3.91438583e-08, 6.37456690e-09,
    1.49837667e-09, 4.76938007e-09, 6.45760445e-08, 5.63120870e-07,
    1.43267112e-06, 1.12378626e-06, 4.60908860e-07, 1.24808552e-07,
    2.13253673e-08, 3.47498214e-09, 1.00969875e-09, 6.55287818e-10,
    3.33454768e-08, 2.76259704e-08, 8.69257458e-09, 1.20744199e-09,
    5.48610153e-10, 4.29908481e-09, 7.93506290e-08, 4.97369614e-07,
    1.13030909e-06, 1.13667547e-06, 5.88153087e-07, 1.74102785e-07,
    2.68079999e-08, 2.24805331e-09, 1.26610775e-10, 1.93090220e-11,
    3.01990679e-08, 1.35637407e-08, 2.98717135e-09, 1.03392333e-09,
    1.88117066e-09, 9.15454669e-09, 9.43653101e-08, 3.02871943e-07,
    4.53760958e-07, 5.28215530e-07, 3.03483726e-07, 8.21951566e-08,
    1.16228288e-08, 9.46495987e-10, 4.60231019e-11, 2.33427108e-12,
    5.37131222e-09, 1.76428613e-09, 7.34604460e-10, 1.88579403e-09,
    6.76732565e-09, 2.39319556e-08, 9.06055282e-08, 1.25184976e-07,
    1.16829916e-07, 1.18547217e-07, 6.28430963e-08, 1.24074959e-08,
    1.33704691e-09, 1.06165013e-10, 7.26539870e-12, 3.85207647e-13,
    2.89937582e-10, 1.44541565e-10, 4.01145213e-10, 2.01216806e-09,
    1.03227353e-08, 3.80664560e-08, 8.88739786e-08, 4.28656793e-08,
    2.10956745e-08, 1.56088056e-08, 6.44254785e-09, 7.72539736e-10,
    5.24972382e-11, 3.80855389e-12, 2.66091352e-13, 1.45377508e-14,
    1.44174138e-11, 4.31674340e-11, 2.18893365e-10, 1.11573835e-09,
    6.51245785e-09, 2.61738004e-08, 5.68376585e-08, 1.87213235e-08,
    3.82846454e-09, 1.72107434e-09, 5.57856285e-10, 5.77119331e-11,
    2.32827591e-12, 1.02709853e-13, 5.66722266e-15, 3.00080561e-16
])

monitoring_probs = np.array([
    3.48365127e-16, 1.21874779e-14, 9.58313326e-14, 8.34264663e-14,
    6.97627581e-14, 2.65459161e-12, 9.41464937e-11, 3.17768522e-10,
    2.01165951e-10, 2.55814027e-11, 1.85113478e-12, 1.87057822e-12,
    2.91794028e-11, 2.27324318e-10, 2.45145108e-10, 5.60893519e-11,
    6.82715942e-15, 1.79599816e-13, 1.02678408e-12, 6.97415905e-13,
    3.66052333e-13, 3.58946208e-12, 1.01230314e-10, 5.41820667e-10,
    5.48723432e-10, 1.41528069e-10, 3.62387281e-11, 1.05988464e-10,
    1.93945868e-09, 1.28594369e-08, 9.85561986e-09, 1.71484198e-09,
    6.64830857e-14, 1.37875000e-12, 6.78721211e-12, 4.47092566e-12,
    2.07441799e-12, 3.87634705e-12, 4.94841549e-11, 4.34923616e-10,
    1.05197143e-09, 9.80216551e-10, 7.54981310e-10, 5.05058569e-09,
    1.03621143e-07, 5.76601933e-07, 3.17431590e-07, 4.64232303e-08,
    3.50161745e-13, 5.16449110e-12, 2.50279905e-11, 2.17153834e-11,
    1.00277932e-11, 5.08529444e-12, 2.29613727e-11, 4.08434300e-10,
    2.52752512e-09, 5.76556340e-09, 1.16431888e-08, 5.96287592e-08,
    1.05577720e-06, 4.87194865e-06, 2.83691028e-06, 8.39672238e-07,
    2.68830281e-12, 4.14385872e-11, 2.38483343e-10, 3.78575437e-10,
    1.44790202e-10, 2.45259293e-11, 3.15657709e-11, 5.48596675e-10,
    5.43305503e-09, 3.42425676e-08, 1.25975750e-07, 3.59220466e-07,
    3.32433708e-06, 1.30324263e-05, 1.83645979e-05, 1.46657345e-05,
    4.68198833e-11, 8.76043132e-10, 5.64654049e-09, 1.09989705e-08,
    5.02262341e-09, 6.15692489e-10, 7.17498391e-10, 8.78682352e-09,
    8.96556098e-08, 4.17659955e-07, 1.22185884e-06, 8.08094786e-06,
    5.79261669e-05, 2.93505792e-04, 7.84703471e-04, 7.55021406e-04,
    7.24750185e-10, 1.56034099e-08, 8.58495819e-08, 1.15337049e-07,
    4.85248046e-08, 1.32469664e-08, 3.28190113e-08, 4.88638652e-07,
    6.39622074e-06, 2.42507973e-05, 4.79829328e-05, 2.31029466e-04,
    1.10822199e-03, 6.43108460e-03, 1.90702877e-02, 1.85185142e-02,
    3.44440926e-09, 8.02116862e-08, 4.17405252e-07, 3.80649391e-07,
    1.34329136e-07, 8.76893586e-08, 4.97683760e-07, 1.13215373e-05,
    2.13125231e-04, 1.12870065e-03, 1.82738388e-03, 2.79599640e-03,
    5.05208541e-03, 1.63486879e-02, 4.87248191e-02, 5.09871099e-02,
    3.90415233e-09, 1.00870168e-07, 6.56416199e-07, 8.69120642e-07,
    5.63059184e-07, 8.12327600e-07, 5.07743137e-06, 1.35333582e-04,
    3.63156515e-03, 2.31968068e-02, 2.76375115e-02, 1.33766885e-02,
    9.18014619e-03, 8.18165600e-03, 1.45995578e-02, 1.70469837e-02,
    1.02829796e-09, 4.62797378e-08, 7.72930051e-07, 2.66332466e-06,
    3.40114944e-06, 6.52142622e-06, 3.16441482e-05, 4.11051714e-04,
    9.71381152e-03, 6.82912579e-02, 9.96622646e-02, 3.56601790e-02,
    7.90181337e-03, 1.73030880e-03, 6.45667481e-04, 5.14162194e-04,
    4.15681807e-10, 2.68550285e-08, 6.21803286e-07, 3.33558207e-06,
    7.91834160e-06, 1.86129289e-05, 6.38891645e-05, 3.02545769e-04,
    5.56640697e-03, 5.12454888e-02, 1.16196729e-01, 5.46420962e-02,
    6.61409907e-03, 3.74067916e-04, 2.52108285e-05, 3.88814561e-06,
    3.11839730e-10, 1.35399566e-08, 2.37862816e-07, 1.71858795e-06,
    6.67976587e-06, 1.76485153e-05, 4.56623842e-05, 1.21588570e-04,
    1.45310826e-03, 1.69690909e-02, 5.80084802e-02, 4.20595454e-02,
    7.76999489e-03, 3.89188582e-04, 9.32281047e-06, 3.44417477e-07,
    1.40531128e-10, 2.95039661e-09, 3.74955692e-08, 3.31359092e-07,
    1.96464601e-06, 6.59668048e-06, 1.50483008e-05, 3.66394674e-05,
    3.67468216e-04, 4.66200657e-03, 2.33381203e-02, 3.27437023e-02,
    1.35546881e-02, 1.35903692e-03, 3.40771934e-05, 5.19533589e-07,
    1.06969056e-11, 1.67120116e-10, 2.57592702e-09, 5.05340237e-08,
    7.46236834e-07, 3.51545610e-06, 4.60566091e-06, 7.97025415e-06,
    6.91795928e-05, 1.26188625e-03, 8.70656031e-03, 1.76773555e-02,
    1.02130825e-02, 1.66241890e-03, 7.31458068e-05, 1.25072661e-06,
    3.03138802e-13, 7.41234685e-12, 3.55783981e-10, 1.42761574e-08,
    2.83198787e-07, 1.73662764e-06, 2.64197424e-06, 1.51218981e-06,
    4.57008594e-06, 9.47268941e-05, 9.01281301e-04, 2.40166321e-03,
    1.90878460e-03, 4.77833233e-04, 2.78353146e-05, 5.37288908e-07,
    1.16633388e-14, 1.04199744e-12, 7.74979472e-11, 2.88085285e-09,
    5.39107469e-08, 5.48035220e-07, 1.11846726e-06, 2.97802935e-07,
    2.35318218e-07, 2.81078187e-06, 3.06040732e-05, 1.24730469e-04,
    1.72955900e-04, 5.87396348e-05, 3.85034531e-06, 8.00794912e-08
])

postdict_probs = np.array([
    3.22115138e-01, 1.45178985e-01, 3.06673277e-02, 2.54168612e-03,
    1.14251442e-04, 3.95167908e-05, 3.86806695e-05, 3.86772436e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    1.45178985e-01, 6.54446022e-02, 1.38411505e-02, 1.16663138e-03,
    7.27339438e-05, 3.90555737e-05, 3.86787846e-05, 3.86772408e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.06673277e-02, 1.38411505e-02, 2.95138383e-03, 2.76707003e-04,
    4.58641526e-05, 3.87570777e-05, 3.86775647e-05, 3.86772389e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    2.54168612e-03, 1.16663138e-03, 2.76707003e-04, 5.81293072e-05,
    3.92645614e-05, 3.86837630e-05, 3.86772651e-05, 3.86772385e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    1.14251442e-04, 7.27339438e-05, 4.58641526e-05, 3.92645614e-05,
    3.86949717e-05, 3.86774354e-05, 3.86772393e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.95167908e-05, 3.90555737e-05, 3.87570777e-05, 3.86837630e-05,
    3.86774354e-05, 3.86772406e-05, 3.86772385e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86806695e-05, 3.86787846e-05, 3.86775647e-05, 3.86772651e-05,
    3.86772393e-05, 3.86772385e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772436e-05, 3.86772408e-05, 3.86772389e-05, 3.86772385e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05,
    3.86772384e-05, 3.86772384e-05, 3.86772384e-05, 3.86772384e-05
])

backwards_probs = np.array([
    7.57005067e-02, 1.15843338e-01, 1.22501112e-01, 7.20993771e-02,
    2.26274721e-02, 4.05414793e-03, 5.21813841e-04, 1.00031355e-04,
    5.89045827e-05, 5.09891101e-05, 3.31983928e-05, 1.41605173e-05,
    3.95522297e-06, 7.55379409e-07, 1.15514172e-07, 2.06236320e-08,
    5.49959143e-02, 8.53432167e-02, 9.20866316e-02, 5.57585378e-02,
    1.81781267e-02, 3.38013070e-03, 4.45611448e-04, 1.01768299e-04,
    8.37215748e-05, 8.09656277e-05, 5.22696813e-05, 2.08248835e-05,
    5.26011694e-06, 9.14728108e-07, 1.36682282e-07, 2.68129206e-08,
    3.01200161e-02, 4.70761552e-02, 5.16730590e-02, 3.22040284e-02,
    1.09216969e-02, 2.10321017e-03, 2.83472788e-04, 8.58010207e-05,
    1.00983486e-04, 1.08251443e-04, 7.07858016e-05, 2.73114401e-05,
    6.49939211e-06, 1.06939025e-06, 1.57958699e-07, 3.17143775e-08,
    1.22980618e-02, 1.85867159e-02, 2.01162484e-02, 1.26059159e-02,
    4.35899712e-03, 8.54749368e-04, 1.17502369e-04, 5.06378183e-05,
    7.93478118e-05, 9.29869532e-05, 6.34514719e-05, 2.54114258e-05,
    6.49423174e-06, 1.22513429e-06, 1.97944499e-07, 3.44770001e-08,
    4.19511304e-03, 5.65637811e-03, 5.67290247e-03, 3.43118958e-03,
    1.18216018e-03, 2.35608840e-04, 3.36370083e-05, 1.92472869e-05,
    3.62754475e-05, 4.64885526e-05, 3.50774218e-05, 1.70219361e-05,
    6.16330501e-06, 1.71678149e-06, 3.29263243e-07, 4.77158945e-08,
    1.52972454e-03, 1.80341936e-03, 1.64984057e-03, 9.72004993e-04,
    3.50547467e-04, 7.94529586e-05, 1.35664160e-05, 6.03059455e-06,
    1.04909584e-05, 1.49262301e-05, 1.45544058e-05, 1.11824164e-05,
    6.48587605e-06, 2.36322402e-06, 4.89693509e-07, 6.63494570e-08,
    6.67315919e-04, 7.72310426e-04, 7.14235025e-04, 4.43494647e-04,
    1.78720950e-04, 5.03296321e-05, 1.29430983e-05, 6.10039090e-06,
    6.44552648e-06, 7.34392090e-06, 7.88804153e-06, 7.85664686e-06,
    5.39558546e-06, 2.09569589e-06, 4.40266815e-07, 5.86867681e-08,
    2.72739136e-04, 3.17464190e-04, 2.97799844e-04, 1.90228516e-04,
    8.25448241e-05, 2.92638758e-05, 1.38525163e-05, 1.28695838e-05,
    1.39873103e-05, 1.12094153e-05, 6.95905417e-06, 4.52541734e-06,
    2.69061719e-06, 1.01124593e-06, 2.11107227e-07, 2.81771078e-08,
    8.03245001e-05, 9.04646809e-05, 8.21770779e-05, 5.17952469e-05,
    2.40515545e-05, 1.23658819e-05, 1.30626487e-05, 2.03307965e-05,
    2.41543432e-05, 1.73652014e-05, 7.60011469e-06, 2.48283339e-06,
    8.41492525e-07, 2.59658975e-07, 5.21676022e-08, 7.07491105e-09,
    1.51138359e-05, 1.61422995e-05, 1.38317629e-05, 8.41576028e-06,
    4.37487593e-06, 4.27338670e-06, 9.58035564e-06, 1.96350942e-05,
    2.46308474e-05, 1.72051308e-05, 6.74916201e-06, 1.58800165e-06,
    2.70474549e-07, 4.56240132e-08, 7.41078784e-09, 1.00700839e-09,
    1.74859020e-06, 1.76561035e-06, 1.41375460e-06, 8.25464895e-07,
    5.54816974e-07, 1.30410019e-06, 4.64336229e-06, 1.08158943e-05,
    1.40647942e-05, 9.85659411e-06, 3.79707676e-06, 8.37712052e-07,
    1.12349040e-07, 1.06262191e-08, 9.54477613e-10, 1.04849392e-10,
    1.32217379e-07, 1.24248260e-07, 9.11889062e-08, 5.18336898e-08,
    6.58663882e-08, 3.33811313e-07, 1.41660564e-06, 3.44229175e-06,
    4.56286974e-06, 3.25377129e-06, 1.27925849e-06, 2.87773122e-07,
    3.84299303e-08, 3.22526347e-09, 1.97003928e-10, 1.30227898e-11,
    1.12895888e-08, 8.78708002e-09, 5.24749126e-09, 4.01692443e-09,
    1.74048722e-08, 9.88223178e-08, 3.62240141e-07, 7.89287086e-07,
    9.89468225e-07, 6.97871782e-07, 2.79405568e-07, 6.48695297e-08,
    8.96170122e-09, 7.64387081e-10, 4.39408681e-11, 2.23722428e-12,
    2.27405760e-09, 1.46961268e-09, 8.42121030e-10, 2.21976613e-09,
    1.32670035e-08, 5.48559617e-08, 1.39003503e-07, 2.19310861e-07,
    2.19031238e-07, 1.36903642e-07, 5.23219718e-08, 1.19592238e-08,
    1.63270290e-09, 1.36298085e-10, 7.53071832e-12, 3.50455790e-13,
    4.53284948e-10, 2.88953962e-10, 3.12560821e-10, 1.82146927e-09,
    1.02252049e-08, 3.52045943e-08, 6.97429329e-08, 8.25577383e-08,
    6.32224450e-08, 3.27154550e-08, 1.11926224e-08, 2.37557326e-09,
    3.00407103e-10, 2.26699272e-11, 1.10148481e-12, 4.46178948e-14,
    6.38161123e-11, 4.84357648e-11, 1.56067363e-10, 1.23528688e-09,
    6.69518402e-09, 2.10873135e-08, 3.61919007e-08, 3.47874870e-08,
    2.10418057e-08, 8.92611296e-09, 2.68532679e-09, 5.24724186e-10,
    6.13795477e-11, 4.17318754e-12, 1.73868237e-13, 5.76499795e-15
])

hindsight_probs = np.array([
    1.03760469e-20, 5.88364059e-18, 1.13604338e-15, 2.48773545e-14,
    8.73834506e-14, 1.38270794e-13, 1.73636399e-13, 4.62813336e-13,
    4.87671056e-12, 3.64598864e-11, 8.41540265e-10, 4.21638971e-07,
    2.39213910e-04, 4.36991629e-03, 2.94044407e-03, 2.58939726e-04,
    5.17071231e-17, 1.47869051e-14, 1.28778913e-12, 1.26663897e-11,
    2.32652276e-11, 1.85077221e-11, 1.27846799e-11, 4.14299731e-12,
    2.49779591e-11, 2.85318226e-10, 5.99001966e-09, 6.01027135e-06,
    4.42892412e-03, 8.06564378e-02, 5.43855272e-02, 5.31740886e-03,
    1.20089816e-13, 1.80159643e-11, 7.53093796e-10, 3.75765677e-09,
    3.69290081e-09, 1.40101691e-09, 3.93145325e-10, 4.12067437e-11,
    5.56471127e-11, 9.74035269e-10, 3.18910525e-08, 2.22489736e-05,
    1.68814890e-02, 3.18625375e-01, 2.44498418e-01, 3.11659664e-02,
    5.62742299e-11, 3.77754306e-09, 7.07005048e-08, 2.22902801e-07,
    1.54488460e-07, 3.12494734e-08, 3.10652125e-09, 2.64659396e-10,
    7.73717191e-11, 1.86187578e-09, 1.67140702e-07, 2.42257934e-05,
    5.78890016e-03, 1.02931342e-01, 9.99216996e-02, 1.68197982e-02,
    2.27875346e-09, 7.38928200e-08, 6.98639019e-07, 1.77882476e-06,
    1.36658246e-06, 2.37840316e-07, 9.40035748e-09, 6.15199720e-10,
    2.58066034e-10, 5.84171260e-09, 7.67561979e-07, 3.30922204e-05,
    4.52171794e-04, 3.18929675e-03, 3.10392486e-03, 5.60385498e-04,
    7.48745527e-09, 1.76807194e-07, 1.28671955e-06, 3.13693285e-06,
    3.56676805e-06, 8.56805392e-07, 2.42301124e-08, 8.56640914e-10,
    1.33083721e-09, 1.27640001e-08, 1.23447765e-06, 2.76705415e-05,
    8.00511543e-05, 5.36667157e-05, 2.81133792e-05, 6.91388183e-06,
    4.47407746e-09, 1.01602582e-07, 8.47466544e-07, 1.87603714e-06,
    2.69746180e-06, 1.07998892e-06, 4.06783795e-08, 1.88037866e-09,
    3.24843027e-09, 1.55453454e-08, 7.29952853e-07, 9.65241404e-06,
    1.21082249e-05, 4.60229657e-06, 1.40454527e-06, 5.17690419e-07,
    2.36406224e-09, 5.82256988e-08, 5.17298832e-07, 8.71346413e-07,
    8.83171386e-07, 4.42509909e-07, 3.28999151e-08, 3.53024583e-09,
    3.09356381e-09, 1.55446864e-08, 2.56189384e-07, 2.57253131e-06,
    7.03719791e-06, 1.17358657e-05, 6.24954318e-06, 1.51513605e-06,
    4.37656829e-09, 1.25004830e-07, 7.39080971e-07, 6.15678879e-07,
    3.29654069e-07, 1.74239974e-07, 2.46029137e-08, 2.67294528e-09,
    1.18725864e-09, 1.25869770e-08, 1.14417251e-07, 1.72886338e-06,
    3.52931324e-05, 1.95418201e-04, 1.47172399e-04, 3.23442737e-05,
    1.75894990e-08, 3.17992452e-07, 1.10480972e-06, 5.13231878e-07,
    2.77465830e-07, 2.10438899e-07, 4.18710342e-08, 3.44494204e-09,
    3.98274704e-10, 2.48783808e-09, 2.49619425e-08, 1.35893863e-06,
    9.90946166e-05, 7.69482000e-04, 7.17826580e-04, 1.95335077e-04,
    8.55408217e-08, 8.62830391e-07, 1.65677357e-06, 6.81926939e-07,
    4.70193375e-07, 5.41683405e-07, 1.51708120e-07, 8.92081186e-09,
    2.75541647e-10, 2.63128061e-10, 4.84657478e-09, 4.06132893e-07,
    3.58551405e-05, 2.77207592e-04, 2.39959236e-04, 6.81389186e-05,
    8.51611756e-07, 6.02957520e-06, 6.98049527e-06, 2.64098408e-06,
    2.71569420e-06, 4.56922021e-06, 1.24335465e-06, 3.15208869e-08,
    3.78809004e-10, 4.20277910e-11, 6.18450420e-10, 3.16906152e-08,
    1.90078234e-06, 1.62881689e-05, 1.14930263e-05, 2.24398106e-06,
    5.31504273e-06, 2.15514582e-05, 2.14153243e-05, 1.14954068e-05,
    1.31748709e-05, 1.84906163e-05, 3.90503408e-06, 6.26062984e-08,
    4.82228299e-10, 1.15017676e-11, 2.60074047e-11, 7.59705743e-10,
    2.61355860e-08, 2.07509867e-07, 1.32590207e-07, 1.77561107e-08,
    3.68798421e-06, 1.35800058e-05, 2.30623330e-05, 1.90362624e-05,
    1.38358820e-05, 1.01805247e-05, 1.28034457e-06, 1.40728373e-08,
    9.76434506e-11, 2.38524806e-12, 5.29588174e-13, 5.66790654e-12,
    1.60326609e-10, 7.58802769e-10, 3.28856468e-10, 3.33818715e-11,
    7.24512316e-07, 4.21400911e-06, 1.12723205e-05, 8.99263362e-06,
    3.39897740e-06, 1.08631109e-06, 6.98759404e-08, 5.29337859e-10,
    3.01471771e-12, 1.17368034e-13, 7.31124363e-15, 2.00099772e-14,
    3.37314545e-13, 8.75800309e-13, 2.43150492e-13, 1.81930133e-14,
    1.21561483e-07, 9.27172979e-07, 2.31145066e-06, 1.43638142e-06,
    3.26776668e-07, 5.04328429e-08, 1.57477624e-09, 8.57720959e-12,
    4.58269736e-14, 1.60190275e-15, 5.34520479e-17, 1.00055972e-16,
    4.97236453e-16, 5.64892261e-16, 1.17839416e-16, 6.43542492e-18
])