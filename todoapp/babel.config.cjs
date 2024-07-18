/* eslint-disable */

module.exports = api => {
  const isNode = api.caller(caller => caller && caller.target === 'node');

  return {
    presets: [
      '@quasar/babel-preset-app',
      [
        '@babel/preset-env',
        isNode
          ? { targets: { node: 'current' } }
          : { modules: false }
      ],
      '@babel/preset-typescript',
    ],
    plugins: [
      '@babel/plugin-transform-runtime',
      '@babel/plugin-proposal-class-properties',
    ],
  }
}
