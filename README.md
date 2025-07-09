
---

## 📌 Features

- Predict house prices using:
  - ✅ Land Size (perches)
  - ✅ House Size (sq. ft.)
  - ✅ City
  - ✅ Latitude & Longitude
- Modern responsive frontend
- Flask backend API with AJAX integration
- Real-world data preprocessing & ML training
- CORS-enabled API for frontend communication

---

## 🔍 Dataset Features

| Feature         | Description                     |
|----------------|---------------------------------|
| City           | Extracted from address/location |
| Land Size      | In perches                      |
| House Size     | In square feet                  |
| Latitude/Longitude | For geo-based pricing        |
| Price          | Target variable (LKR)           |

---

## 🤖 ML Model Details

- **Algorithm**: Linear Regression
- **Library**: `scikit-learn`
- **Inputs**: Land size, House size, Latitude, Longitude, City (one-hot)
- **Output**: Predicted house price (LKR)
- **Model saved in**: `model/Realestate_price_prediction_model.pickle`

---

## 🔗 Flask API Endpoints

| Method | Endpoint         | Description                         |
|--------|------------------|-------------------------------------|
| GET    | `/get_city`      | Returns list of all supported cities |
| POST   | `/predict_price` | Returns predicted price in LKR       |

---

## 🖥 Frontend Overview

- Built using HTML, CSS, and jQuery
- Dynamic city dropdown (populated via `/get_city`)
- Inputs for land, house size, lat/lon
- Predict button triggers `/predict_price` API
- Price result is shown instantly in the UI

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/RealEstatePricePredictor.git
cd RealEstatePricePredictor
