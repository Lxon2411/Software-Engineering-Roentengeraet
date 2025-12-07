## Traceability-Matrix Sprint 1
| **Requirement-ID**        | **Komponente**                 | **Klasse(n)**                                 | **Schnittstelle(n)**                                                                       | **Testfall-ID(s)** |
|---------------------------|--------------------------------|-----------------------------------------------|--------------------------------------------------------------------------------------------|--------------------|
| 1.1 (funktional)          | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController``` | ```start_radiation()```, ```stop_radiation()```, ```duration_entry```                      | M1                 |
| 2.1 (funktional)          | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController``` | ```duration_entry.get()```, ```start_radiation()```, ```start()```, ```_run_radiation()``` | I1                 |
| 3.1 (funktional)          | Steuerungslogik, Systemschicht | ```RadiationController```                     | ```update_progress()```, ```stop()```, ```reset_ui```, ```show_finished_message()```       | M3, I3             |
| 5.1 (funktional)          | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController``` | ```update_progress()```, ```progress['value']```, ```progress_label```                     | M2, I2             |
| 1.1<br/>(nichtfunktional) | GUI, Steuerungslogik           | ```Radiation UI```, ```RadiationController``` | -                                                                                          | -                  |
| 1.3<br/>(nichtfunktional) | GUI                            | ```Radiation UI```                            | -                                                                                          | -                  |

