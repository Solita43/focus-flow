import { FormEvent, useState, useEffect } from "react";
import { login, authenticate } from "./store/session";
import { useAppDispatch } from "./store";
import "./App.css";

function App() {
  const dispatch = useAppDispatch();
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [errors, setErrors] = useState<string | null>(null);
  const [isLoaded, setIsLoaded] = useState<boolean>(false);

  useEffect(() => {
    console.log("I'm in the useEffect!")
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, []);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    const data = await dispatch(login({ email, password }));

    console.log(data);
  };

  return (
    <>
      <h1>Welcome Back!</h1>
      <form onSubmit={handleSubmit}>
        {errors && <p className="errors">*{errors}</p>}
        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        <button type="submit" className="login-form">
          Log In
        </button>
      </form>
    </>
  );
}

export default App;
