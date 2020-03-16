import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import io
import urllib, base64

def f(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d
def convertGraphTimage(fig):
    # convert graph into string buffer and then we convert 64 bit code into image
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return uri
class Optimisation():
    def __init__(self):
        self.x = np.linspace(0, 2, 100)
        self.y = 1 / 4 * self.x ** 3 - 3 / 5 * self.x ** 2 + 2 + np.random.randn(self.x.shape[0]) / 20
    def show_nuage(self):
        fig, ax = plt.subplots()
        ax.scatter(self.x, self.y)
        return convertGraphTimage(fig)

    # Définition d'un modele statistique sensé "coller" au dataset ci-dessus
    def getParam(self):
        params, param_cov = optimize.curve_fit(f, self.x, self.y)
        return params
    def showResult(self,params):
        print(params)
        fig, ax = plt.subplots()
        ax.scatter(self.x,self.y)
        ax.plot(self.x, f(self.x, params[0], params[1], params[2], params[3]), c='r', lw=3)
        return  convertGraphTimage(fig)


def main():
    # Création d'un Dataset avec du bruit "normal"
    opt = Optimisation()
    opt.show_nuage()
    # curve_fit permet de trouver les parametres du modele f grace a la méthode des moindres carrés
    params, param_cov = optimize.curve_fit(f, opt.x, opt.y)
    print(params)
    print(param_cov)
    # Visualisation des résultats.
    opt.showResult(params)


if __name__ == '__main__':
    main()