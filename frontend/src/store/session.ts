import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

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
    const response = await fetch("/api/auth/login", {
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
