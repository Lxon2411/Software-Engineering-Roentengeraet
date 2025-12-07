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
            self.ui.show_finished_message(duration)
        else:
            self.ui.show_abort_message(elapsed)
        self.ui.reset_ui()

    def stop(self):
        if self.running:
            self.aborted = True
        self.running = False
