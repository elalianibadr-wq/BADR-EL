import js from "@eslint/js";

export default [
    js.configs.recommended,

    {
        languageOptions: {
            ecmaVersion: "latest",
            sourceType: "module"
        },

        rules: {
            "no-console": "off",
            "semi": ["error", "always"],
            "quotes": ["error", "double"]
        }
    }
];
