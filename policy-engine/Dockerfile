FROM openpolicyagent/opa:latest
COPY policies/ /policies/
EXPOSE 8181
CMD ["run", "--server", "/policies"]
