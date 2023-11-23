from pydantic import BaseModel

class PulsarPredictionRequest(BaseModel):
    Mean_Integrated: float
    SD: float
    EK: float
    Skewness: float
    Mean_DMSNR_Curve: float
    SD_DMSNR_Curve: float
    EK_DMSNR_Curve: float
    Skewness_DMSNR_Curve: float
