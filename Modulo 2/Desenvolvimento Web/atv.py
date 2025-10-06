import streamlit as st


lista = st.columns(4)


with lista[0]:
  if  st.text('soma'):
      numero1=st.text_input('digite um numero para somar ')
      numero2=st.text_input('digite outro numero para somar')
      if st.button('enviar '):


       resultado= int(numero1) + int(numero2)
       st.text(f'o resultado é {resultado}')


with lista[1]:
    if st.text('dividir'):
       numero1=st.text_input('digite um numero para dividir')
       numero2=st.text_input('digite outro numero para dividir')
       if st.button('enviar  '):


        resultado= int(numero1) / int(numero2)
        st.text(f'o resultado é {resultado}')


with lista[2]:
    if st.text('subtrair'):
        numero1=st.text_input('digite um numero para subtrair ')
        numero2=st.text_input('digite outro numero para subtrair')
        if st.button('enviar   '):


         resultado= int(numero1) - int(numero2)
         st.text(f'o resultado é {resultado}')
       


with lista[3]:
    if st.text('multiplicar'):
       numero1=st.text_input('digite um numero para multiplicar')
       numero2=st.text_input('digite outro numero para multiplicar')
       if st.button('enviar    '):


         resultado= int(numero1) * int(numero2)
         st.text(f'o resultado é {resultado}')
