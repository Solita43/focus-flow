import { configureStore } from '@reduxjs/toolkit';
import { useDispatch, TypedUseSelectorHook, useSelector } from 'react-redux';
import { sessionSlice } from './session';

export const store = configureStore({
  reducer: {
    session:sessionSlice.reducer
  }
});

export type AppDispatch = typeof store.dispatch;
export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector:TypedUseSelectorHook<ReturnType<typeof store.getState>>=useSelector;

export type RootState = ReturnType<typeof store.getState>;

