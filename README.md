# Convex Hull Algorithms

Dieses Projekt implementiert zwei klassische Algorithmen zur Berechnung der konvexen Hülle einer Punktmenge in 2D:

- **Graham Scan** - Ein effizienter Algorithmus mit O(n log n) Zeitkomplexität
- **Jarvis March (Gift Wrapping)** - Ein einfacherer Algorithmus mit O(nh) Zeitkomplexität, wobei h die Anzahl der Punkte auf der Hülle ist

Die konvexe Hülle einer Punktmenge ist eines der am meisten untersuchten geometrischen Probleme sowohl in der Algorithmik als auch in der reinen Mathematik. Die Berechnung der konvexen Hülle ist eine grundlegende Operation in der Computergeometrie.

## Features

- ✅ Visuelle Darstellung der Algorithmen Schritt für Schritt
- ✅ Beide Algorithmen vollständig implementiert
- ✅ Interaktive Visualisierung mit matplotlib
- ✅ Sauberer, dokumentierter Code

## Installation

1. Repository klonen:
```bash
git clone <repository-url>
cd convexhull
```

2. Virtuelles Environment erstellen (empfohlen):
```bash
python -m venv venv
```

3. Virtuelles Environment aktivieren:
   - Windows:
   ```bash
   venv\Scripts\activate
   ```
   - Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

## Verwendung

### Graham Scan Algorithmus

```bash
python FindingConvexHullImplementierung/GrahamScan.py [anzahl_punkte]
```

Beispiel:
```bash
python FindingConvexHullImplementierung/GrahamScan.py 50
```

Wenn keine Anzahl angegeben wird, werden Sie zur Eingabe aufgefordert.

### Jarvis March Algorithmus

```bash
python FindingConvexHullImplementierung/JarvisMarch.py [anzahl_punkte]
```

Beispiel:
```bash
python FindingConvexHullImplementierung/JarvisMarch.py 50
```

## Algorithmen

### Graham Scan

Der Graham-Scan-Algorithmus funktioniert in zwei Phasen:
1. **Obere Hülle**: Berechnet den oberen Teil der konvexen Hülle
2. **Untere Hülle**: Berechnet den unteren Teil der konvexen Hülle

**Zeitkomplexität**: O(n log n)  
**Raumkomplexität**: O(n)

### Jarvis March (Gift Wrapping)

Der Jarvis-March-Algorithmus beginnt mit dem linkesten Punkt und "wickelt" die Hülle Schritt für Schritt ein, bis er wieder zum Startpunkt zurückkehrt.

**Zeitkomplexität**: O(nh), wobei h die Anzahl der Punkte auf der Hülle ist  
**Raumkomplexität**: O(n)

## Projektstruktur

```
convexhull/
├── FindingConvexHullImplementierung/
│   ├── GrahamScan.py          # Graham Scan Implementierung
│   └── JarvisMarch.py          # Jarvis March Implementierung
├── requirements.txt            # Python Abhängigkeiten
├── .gitignore                  # Git Ignore Datei
├── Quellen.txt                 # Referenzen und Quellen
└── README.md                   # Diese Datei
```

## Abhängigkeiten

- `numpy >= 1.19.0` - Für numerische Operationen
- `matplotlib >= 3.3.0` - Für die Visualisierung

## Quellen

Die Implementierungen basieren auf folgenden Quellen:
- [Jarvis March Demonstration](https://www.wolframcloud.com/objects/demonstrations/JarvisMarchToFindTheConvexHullOfASetOfPointsIn2D-source.nb)
- [Convex Hull Notes](http://jeffe.cs.illinois.edu/teaching/373/notes/x05-convexhull.pdf)
- [Convex Hull Tutorial](https://learnopencv.com/convex-hull-using-opencv-in-python-and-c/)

## Lizenz

Dieses Projekt wurde als Universitätsprojekt erstellt und ist für Bildungszwecke verfügbar.

## Autor

Universitätsprojekt - für GitHub veröffentlicht
