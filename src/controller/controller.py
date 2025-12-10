import threading
import time


class RadiationController:
    def __init__(self, ui):
        self.ui = ui
        self.running = False
        self.aborted = False
        self.thread = None

    def start(self, duration):
        if self.running:
            return

        self.running = True
        self.aborted = False

        self.thread = threading.Thread(target=self._run_radiation, args=(duration,), daemon=True)
        self.thread.start()
        self.ui.log_message(f"Strahlung gestartet für {duration} s")

    def _run_radiation(self, duration):
        start_time = time.time()
        while self.running:
            elapsed = time.time() - start_time
            if elapsed >= duration:
                break
            self.ui.update_progress(elapsed, duration)
            time.sleep(0.02)

        self.running = False

        if not self.aborted:
            self.ui.update_progress(elapsed, duration)
            self.ui.log_message(f"Strahlung automatisch beendet nach {elapsed:.1f} s")
            self.ui.reset_ui()
            self.ui.show_finished_message(duration)
        else:
            self.ui.log_message(f"Strahlung abgebrochen nach {elapsed:.1f} s")
            self.ui.reset_ui()
            self.ui.show_abort_message(elapsed)


    def stop(self):
        if self.running:
            self.aborted = True
        self.running = False
