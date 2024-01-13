import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { csrfFetch } from "./csrf";

interface UserData {
  id: number;
  username: string;
  email: string;
}

interface SessionState {
  user: UserData | null;
}

const initialState: SessionState = {
  user: null,
};

/*----------------------------Thunks---------------------------------- */

export const authenticate = createAsyncThunk('session/authenticate', async () => {
    const response = await fetch('/accounts/authenticated', {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    if (response.ok) {
      const data: UserData = await response.json();
      return data
    } else {
        const getCSRF = await fetch('/accounts/csrf_cookie')

        if (getCSRF.ok) {
            return 
        } else {
            return {"error": "Sorry there was an error on our end"}
        }
    }
  });

interface LoginResponse {
    message: string;
    data: UserData;
}

interface LoginPayload {
    email: string;
    password: string;
}

export const login = createAsyncThunk(
  "session/login",
  async (payload: LoginPayload) => {
    const { email, password } = payload;
    const response = await csrfFetch("/accounts/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    if (response.ok) {
      const data: LoginResponse = await response.json();
      return data.data;
    } else if (response.status < 500) {
      const data = await response.json();
      // Handle errors if needed
      return data;
    } else {
      // Handle server errors
      return { errors: ["An error occurred. Please try again."] };
    }
  }
);

/* ------------------------ Slice Reducer ---------------------------------- */

export const sessionSlice = createSlice({
  name: "session",
  initialState,
  reducers: {
    removeUser: (state) => {
      state.user = null;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(login.fulfilled, (state, action) => {
        state.user = action.payload
    })
  },
});
