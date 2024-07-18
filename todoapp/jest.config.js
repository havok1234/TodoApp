
module.exports = {
  transform: {
    '^.+\\.js$': 'babel-jest',
    '^.+\\.jsx?$': 'babel-jest', // If you're using JSX
    '^.+\\.tsx?$': 'ts-jest',    // If you're using TypeScript
    '^.+\\.vue$': 'vue-jest',    // If you're using Vue single file components
  },
  moduleFileExtensions: ['js', 'jsx', 'ts', 'tsx', 'json', 'vue'],
  transformIgnorePatterns: [
    '/node_modules/(?!(quasar)/)',
  ],
  testEnvironment: 'jest-environment-jsdom',
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  testEnvironmentOptions: {
    customExportConditions: ["node", "node-addons"],
 },
};
