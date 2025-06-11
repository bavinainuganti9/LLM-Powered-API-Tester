import React, { useEffect, useRef } from "react";
import * as monaco from "monaco-editor";

export default function CodeEditor({ code }) {
  const editorRef = useRef();

  useEffect(() => {
    if (!editorRef.current) return;

    const editor = monaco.editor.create(editorRef.current, {
      value: code || "// Your test code will appear here",
      language: "python",
      theme: "vs-dark",
      automaticLayout: true,
    });

    return () => editor.dispose();
  }, [code]);

  return <div ref={editorRef} style={{ height: "400px", width: "100%" }} />;
}
