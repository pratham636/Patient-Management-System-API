# 🏥 Patient Management System API

A lightweight, robust FastAPI application designed to manage patient records. This API supports full CRUD (Create, Read, Update, Delete) operations, automatic BMI calculation, and data persistence using a JSON-based storage system.

## 🚀 Features
* **Automated Health Metrics:** Automatically calculates BMI and provides a health verdict (Underweight, Normal, Overweight, Obese).
* **Data Validation:** Strict data validation using Pydantic models.
* **Sorting Engine:** Sort patients by Height, Weight, or BMI in ascending or descending order.
* **Persistence:** Local JSON file storage ensures data is saved between restarts.
* **Auto-Documentation:** Interactive API documentation via Swagger UI.

## 🛠️ Tech Stack
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Validation:** [Pydantic v2](https://docs.pydantic.dev/)
* **Language:** Python 3.9+

## 📁 Project Structure
```text
patient_api/
├──app/
├   ├── main.py          # Route handlers and FastAPI instance
├   ├── schemas.py       # Pydantic data models & logic
├   ├── database.py      # JSON file I/O operations
├   └── patients.json    # Local data storage (Database)
├── Dockerfile
├── README.md
├── requirements.txt

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pratham636/Patient-Management-System-API.git
   cd Patient-Management-System-API


2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn pydantic

4. **Run the application:**
   ```bash
   uvicorn app.main:app --reload

5. **Access the API:**
   * **Interactive Swagger Docs:** http://127.0.0.1:8000/docs
   * **Alternative ReDoc:** http://127.0.0.1:8000/redoc

> **Note:** The server must remain running in your terminal for the API to work.
