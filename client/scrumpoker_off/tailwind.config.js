module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: 'media',
  theme: {
    minWidth:{
      '400': '400px'
    },
    extend: {
      backgroundImage: theme => ({
        'sw-logo': "url('http://sebastianweszler.com/assets/images/logo.png')"
      })
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
