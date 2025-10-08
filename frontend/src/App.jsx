import { useState } from "react";
import axios from "axios";

function App() {
  const [formData, setFormData] = useState({
    Temperature: "",
    RH: "",
    Ws: "",
    Rain: "",
    FFMC: "",
    DMC: "",
    ISI: "",
    Classes: "",
    Region: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:8080/predict", formData);
      setResult(res.data.prediction);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>FWI Prediction</h1>
      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <input
            key={key}
            type="text"
            name={key}
            placeholder={key}
            value={formData[key]}
            onChange={handleChange}
            required
            style={{ margin: "5px", padding: "8px", width: "200px" }}
          />
        ))}
        <br />
        <button type="submit" style={{ padding: "10px 20px", marginTop: "10px" }}>
          Predict
        </button>
      </form>

      {result !== null && (
        <h2 style={{ marginTop: "20px" }}>Result: {result}</h2>
      )}
    </div>
  );
}

export default App;
