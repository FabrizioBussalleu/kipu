# Gestión del proyecto Kipu

## Flujo de trabajo en el repositorio

- Repositorio: https://github.com/FabrizioBussalleu/kipu
- Ramas: `main` (entregas), `develop` (integración) y una rama `feature/...` por avance. Los cambios entran a `develop` y luego a `main` mediante pull requests revisados por otro integrante.
- Integración continua: `.github/workflows/pruebas.yml` ejecuta la verificación de la gramática, las pruebas y las derivaciones en Ubuntu y Windows en cada push y pull request.
- Convención de nombres de documentos: `[AAAA-MM-DD]_[ÁREA]_[PROYECTO]_[TIPO]_[CONTENIDO]_[vX.X]`.

## Tablero de tareas

Este tablero puede replicarse en GitHub Projects (una tarjeta por fila).

| Hito | Tarea | Responsable | Estado |
|---|---|---|---|
| 1 | Idea del lenguaje y visto bueno del docente | Equipo | Hecho |
| 1 | Problemática, objetivos y construcciones (5 ejemplos c/u) | Fabrizio Bussalleu | Hecho |
| 1 | Léxico (token: lexemas) y analizador léxico | Jose Luis Sancho | Hecho |
| 1 | Gramáticas, derivaciones y analizador sintáctico | Jose Luis Sancho | Hecho |
| 1 | Analizador semántico parcial (5 errores) | Marco Cabrera | Hecho |
| 1 | Informe, presentación y video | Equipo | Hecho |
| 2 | Reescribir Kipu.g4 en la forma estándar del curso | Jose Luis Sancho | Hecho |
| 2 | Regenerar y verificar las 28 derivaciones | Jose Luis Sancho | Hecho |
| 2 | Construcción del AST | Marco Cabrera | Hecho |
| 2 | Analizador semántico completo (14 errores) | Marco Cabrera | Hecho |
| 2 | Arquitectura del compilador | Marco Cabrera | Hecho |
| 2 | Plan de validación y pruebas automáticas | Equipo | Hecho |
| 2 | Avance de generación de LLVM IR y ejecución JIT | Marco Cabrera | Hecho |
| 2 | Informe, presentación, guiones y video del Hito 2 | Fabrizio Bussalleu | En curso (falta grabar el video) |
| 3 | LLVM IR para reglas, llamadas, retornar y leer | Marco Cabrera | Pendiente |
| 3 | Ejecutables nativos con clang en Windows y Linux | Jose Luis Sancho | Pendiente |
| 3 | Resultados de la validación y conclusiones | Equipo | Pendiente |
| 3 | Informe final, presentación, video y sustentación | Equipo | Pendiente |

Los responsables son una propuesta inicial; el equipo puede ajustarlos.
