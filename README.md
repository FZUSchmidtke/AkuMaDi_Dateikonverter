# Datenkonvertierer
Dieses kleine Skript liest `.npz` Dateien ein und konvertiert sie in `.csv`
Dateien. Zur Nutzung wird eine [Python-Installation](https://www.python.org/)
benötigt.

## Installation
Doppelklicken Sie die Datei `install.bat`, um das Programm einzurichten.

## Ausführung
Das Programm wird durch Doppelklicken auf `run.bat` gestartet.
Es wird nach dem zu durchsuchenden Dateipfad gefragt. Hier gibt es 2 Möglichkeiten:
1. Es kann ein lokaler Pfad aus dem Datei-Explorer kopiert werden.
2. Ein Ordner mit den zu kopierenden Dateien kann in das Programmverzeichnis kopiert werden.
In diesem Fall muss als Pfad im Program `.` (ein einzelner Punkt) eingegeben werden.

Unabhängig von der Methode durchsucht das Programm alle Unterverzeichnisse im angegebenen Pfad
und konvertiert die Daten. Eine CSV-Datei wird im selben Verzeichnis wie die ursprüngliche Datei
erstellt.

## Dateistruktur
| time | channel1 | channel2 |
|------|----------|----------|
| 0.0  | 0.0      | 0.0      |

Die CSV Datei enthält 3 Spalten:
* `time`: Relative Zeit ab Aufnahmebeginn (in Sekunden)
* `channel1`: gemessene Amplitude des Kanal 1 (in Volt)
* `channel2`: gemessene Amplitude des Kanal 2 (in Volt)