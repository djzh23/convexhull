"""
Jarvis March (Gift Wrapping) Algorithmus zur Berechnung der konvexen Hülle.

Dieses Skript implementiert den Jarvis-March-Algorithmus (auch bekannt als
Gift Wrapping) mit visueller Darstellung zur Berechnung der konvexen Hülle.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt


def ccw(p1, p2, p3):
    """
    Prüft, ob drei Punkte eine Rechtskurve (clockwise turn) bilden.
    
    Args:
        p1: Erster Punkt als [x, y] Array
        p2: Zweiter Punkt als [x, y] Array
        p3: Dritter Punkt als [x, y] Array
    
    Returns:
        True wenn clockwise (Rechtskurve), False wenn counter-clockwise (Linkskurve)
    """
    if (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0]):
        return True
    return False


def jarvis_march(points):
    """
    Berechnet die konvexe Hülle einer Punktmenge mit dem Jarvis-March-Algorithmus.
    
    Der Algorithmus beginnt mit dem linkesten Punkt und "wickelt" die Hülle
    Schritt für Schritt ein, bis er wieder zum Startpunkt zurückkehrt.
    
    Args:
        points: NumPy-Array von Punkten als [[x1, y1], [x2, y2], ...]
    
    Returns:
        NumPy-Array der Punkte auf der konvexen Hülle
    """
    plt.figure()  # Figur definieren
    n = len(points)
    hull = [None] * n
    
    # Finde den linkesten Punkt (kleinste x-Koordinate)
    leftmost_idx = np.where(points[:, 0] == np.min(points[:, 0]))[0][0]
    point_on_hull = points[leftmost_idx]  # Punkt ganz links, Teil der Hülle
    
    i = 0
    while True:
        hull[i] = point_on_hull
        # Initialisiere Endpunkt für die Prüfung mit den nächsten Punkten
        endpoint = points[0]
        for j in range(1, n):
            if ((endpoint[0] == point_on_hull[0] and endpoint[1] == point_on_hull[1]) or
                    not ccw(points[j], hull[i], endpoint)):
                # Update Endpunkt falls der Punkt gefunden ist
                endpoint = points[j]
        i += 1
        point_on_hull = endpoint
        current_hull = np.array([hull[k] for k in range(n) if hull[k] is not None])
        
        # Plot der aktuellen Hülle und aller Punkte
        plot_current_hull(current_hull, points)
        
        # Prüfe ob wir wieder am Startpunkt angekommen sind
        if endpoint[0] == hull[0][0] and endpoint[1] == hull[0][1]:
            break
    
    # Entferne None-Einträge am Ende
    while hull[-1] is None:
        del hull[-1]
    hull = np.array(hull)
    
    # Finale Hülle plotten
    plot_final_hull(hull, points)
    return hull


def plot_final_hull(hull, points):
    """
    Plottet die finale konvexe Hülle mit geschlossenem Polygon.
    
    Args:
        hull: NumPy-Array der Punkte auf der Hülle
        points: NumPy-Array aller Punkte
    """
    plt.clf()
    plt.plot(hull[:, 0], hull[:, 1], 'b-', picker=5)
    # Schließe das Polygon (letzter Punkt zu erstem Punkt)
    plt.plot([hull[-1, 0], hull[0, 0]], [hull[-1, 1], hull[0, 1]], 'b-', picker=5)
    plt.plot(points[:, 0], points[:, 1], ".r")
    plt.axis('off')
    plt.show(block=False)
    plt.pause(0.0000001)


def plot_current_hull(hull, points):
    """
    Plottet die aktuelle Hülle während der Berechnung.
    
    Args:
        hull: NumPy-Array der aktuellen Hülle
        points: NumPy-Array aller Punkte
    """
    plt.clf()  # Plot löschen
    plt.plot(hull[:, 0], hull[:, 1], 'b-', picker=5)  # Linien plotten
    plt.plot(points[:, 0], points[:, 1], ".r")  # Punkte plotten
    plt.axis('off')  # Keine Achsen
    plt.show(block=False)  # Plot anzeigen (nicht blockierend)
    plt.pause(0.0000001)  # Kurze Pause


def main():
    """
    Hauptfunktion: Liest die Anzahl der Punkte ein und berechnet die konvexe Hülle.
    """
    try:
        n = int(sys.argv[1])
    except (IndexError, ValueError):
        n = int(input("Anzahl der Punkte N eingeben: "))
    
    # Zufällige Punktmenge mit Koordinaten in [0, 300) x [0, 300)
    points = np.array([(np.random.randint(0, 300), np.random.randint(0, 300)) 
                      for _ in range(n)])
    hull = jarvis_march(points)
    
    # Finale Visualisierung mit geschlossenem Polygon
    plt.plot(hull[:, 0], hull[:, 1], 'b-', picker=5)
    plt.plot([hull[-1, 0], hull[0, 0]], [hull[-1, 1], hull[0, 1]], 'b-', picker=5)
    plt.plot(points[:, 0], points[:, 1], ".r")
    plt.axis('off')
    plt.show()
    print(f"Konvexe Hülle berechnet mit {len(hull)} Punkten.")


if __name__ == '__main__':
    main()
