"""
Graham Scan Algorithm zur Berechnung der konvexen Hülle einer Punktmenge.

Dieses Skript implementiert den Graham-Scan-Algorithmus mit visueller Darstellung
jedes Schritts zur Berechnung der konvexen Hülle.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt


def right_turn(p1, p2, p3):
    """
    Prüft, ob drei Punkte eine Rechtskurve (clockwise turn) bilden.
    
    Berechnet die Determinante einer 3x3 Matrix:
    [p1(x) p1(y) 1]
    [p2(x) p2(y) 1]
    [p3(x) p3(y) 1]
    
    Args:
        p1: Erster Punkt als [x, y] Liste
        p2: Zweiter Punkt als [x, y] Liste
        p3: Dritter Punkt als [x, y] Liste
    
    Returns:
        True wenn counter-clockwise (Linkskurve), False wenn clockwise (Rechtskurve)
    """
    if (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0]):
        return False
    return True


def graham_scan(points):
    """
    Berechnet die konvexe Hülle einer Punktmenge mit dem Graham-Scan-Algorithmus.
    
    Der Algorithmus funktioniert in zwei Phasen:
    1. Berechnung des oberen Teils der Hülle
    2. Berechnung des unteren Teils der Hülle
    
    Args:
        points: Liste von Punkten als [(x1, y1), (x2, y2), ...]
    
    Returns:
        NumPy-Array der Punkte auf der konvexen Hülle
    """
    points.sort()  # Punkte sortieren
    points = np.array(points)  # In NumPy-Array konvertieren
    plt.figure()  # Neue Figur erstellen
    
    # Obere Hülle berechnen
    l_upper = [points[0], points[1]]
    for i in range(2, len(points)):
        l_upper.append(points[i])
        while len(l_upper) > 2 and not right_turn(l_upper[-1], l_upper[-2], l_upper[-3]):
            del l_upper[-2]
        l = np.array(l_upper)
        plt.clf()  # Plot löschen
        plt.plot(l[:, 0], l[:, 1], 'b-', picker=5)  # Linien plotten
        plt.plot(points[:, 0], points[:, 1], ".r")  # Punkte plotten
        plt.axis('off')  # Keine Achsen
        plt.show(block=False)  # Plot anzeigen (nicht blockierend)
        plt.pause(0.0000001)  # Kurze Pause
    
    # Untere Hülle berechnen
    l_lower = [points[-1], points[-2]]
    for i in range(len(points) - 3, -1, -1):
        l_lower.append(points[i])
        while len(l_lower) > 2 and not right_turn(l_lower[-1], l_lower[-2], l_lower[-3]):
            del l_lower[-2]
        l = np.array(l_upper + l_lower)
        plt.clf()  # Plot löschen
        plt.plot(l[:, 0], l[:, 1], 'b-', picker=8)  # Linien plotten
        plt.plot(points[:, 0], points[:, 1], ".r")  # Punkte plotten
        plt.axis('off')  # Keine Achsen
        plt.show(block=False)  # Plot anzeigen (nicht blockierend)
        plt.pause(0.0000001)  # Kurze Pause
    
    # Ersten und letzten Punkt der unteren Hülle entfernen (doppelt)
    del l_lower[0]
    del l_lower[-1]
    l = l_upper + l_lower  # Vollständige Hülle zusammenfügen
    plt.axis('on')
    plt.show()
    return np.array(l)


def main():
    """
    Hauptfunktion: Liest die Anzahl der Punkte ein und berechnet die konvexe Hülle.
    """
    try:
        n = int(sys.argv[1])
    except (IndexError, ValueError):
        n = int(input("Anzahl der Punkte N eingeben: "))

    # Zufällige Punktmenge mit Koordinaten in [-300, 300) x [-300, 300)
    points = [(np.random.randint(-300, 300), np.random.randint(-300, 300)) 
              for _ in range(n)]
    hull = graham_scan(points)
    print(f"Konvexe Hülle berechnet mit {len(hull)} Punkten.")


if __name__ == '__main__':
    main()
