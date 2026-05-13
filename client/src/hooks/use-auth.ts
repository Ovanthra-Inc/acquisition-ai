"use client"

import { useEffect } from 'react'
import { useAppDispatch, useAppSelector } from '@/lib/hooks'
import { setCredentials, logout } from '@/lib/features/auth/authSlice'
import { authApi } from '@/lib/api'
import { useQuery } from '@tanstack/react-query'

export function useAuth() {
  const dispatch = useAppDispatch()
  const { user, isAuthenticated, token } = useAppSelector((state) => state.auth)

  const { data, isLoading, error } = useQuery({
    queryKey: ['auth-me'],
    queryFn: () => authApi.me().then(res => res.data),
    enabled: !!token,
  })

  useEffect(() => {
    if (data) {
      dispatch(setCredentials({ user: data, token: token! }))
    }
    if (error) {
      dispatch(logout())
      localStorage.removeItem('token')
    }
  }, [data, error, dispatch, token])

  const login = () => authApi.login()
  
  const handleLogout = () => {
    dispatch(logout())
    localStorage.removeItem('token')
  }

  return { user, isAuthenticated, isLoading, login, logout: handleLogout }
}
