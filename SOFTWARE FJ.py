# =========================================================
# SISTEMA DE GESTIÓN SOFTWARE FJ - UNAD
# =========================================================
import logging
from abc import ABC, abstractmethod
from datetime import datetime

# =========================================================
# CONFIGURACIÓN DE LOGS (Archivo de registro de errores)
# =========================================================
logging.basicConfig(
    filename='registro_eventos.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# =========================================================
# EXCEPCIONES PERSONALIZADAS
# =========================================================
class ErrorGestionSoftware(Exception):
    """Clase base para excepciones del sistema."""
    pass

class ReservaInvalidaError(ErrorGestionSoftware):
    """Se lanza cuando una reserva no cumple los requisitos."""
    pass

class DatosClienteError(ErrorGestionSoftware):
    """Se lanza cuando los datos del cliente son incorrectos."""
    pass